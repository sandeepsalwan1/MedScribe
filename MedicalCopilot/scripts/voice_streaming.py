import asyncio
import signal
from dataclasses import dataclass
from datetime import datetime, timezone

import click
import requests
from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    LiveOptions,
    LiveTranscriptionEvents,
    Microphone,
)
from deepgram.utils import verboselogs
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEEPGRAM_API_KEY: str = "deepgram-api-key"
    BATCH_SIZE: int = 10

    class Config:
        env_file = ".env"


@dataclass
class SentenceChunk:
    text: str
    created_at: datetime


class TranscriptCollector:
    def __init__(self, batch_size: int = 10):
        self.batch_size = batch_size
        self.reset()

    def reset(self):
        self.transcript_parts = []

    def add_part(self, part: str):
        self.transcript_parts.append(
            SentenceChunk(text=part, created_at=datetime.now(tz=timezone.utc))
        )

    def length_check(self) -> bool:
        if len(self.transcript_parts) > 1:
            return (
                self.transcript_parts[-1].created_at
                - self.transcript_parts[0].created_at
            ).seconds > self.batch_size
        return (
            datetime.now(tz=timezone.utc) - self.transcript_parts[0].created_at.second
            > self.batch_size
        )

    def get_full_transcript(self):
        transcript_text = "\n".join([part.text for part in self.transcript_parts])

        if self.transcript_parts:
            end_time = self.transcript_parts[-1].created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            start_time = self.transcript_parts[0].created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        else:
            # Handle the case where there are no transcript parts
            end_time = start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return transcript_text, (end_time, start_time)


async def get_transcript(
    api_key: str,
    transcript_collector: TranscriptCollector,
    start_time: datetime = datetime.now(tz=timezone.utc),
):
    shutdown_event = asyncio.Event()

    def signal_handler():
        click.echo("\nShutting down gracefully...", err=True)
        shutdown_event.set()

    try:
        config = DeepgramClientOptions(
            options={"keepalive": "true"}, verbose=verboselogs.ERROR
        )
        deepgram: DeepgramClient = DeepgramClient(api_key=api_key, config=config)

        dg_connection = deepgram.listen.asyncwebsocket.v("1")

        messages = 0

        async def on_message(self, result, **kwargs):

            sentence = result.channel.alternatives[0].transcript

            if sentence:
                print(f"Received: {sentence}")
                transcript_collector.add_part(sentence)

                result = requests.post(
                            url="http://localhost:8000/text-chunk/",
                            json={"text": sentence},
                        )


        async def on_error(self, error, **kwargs):
            click.echo(f"\n\n{error}\n\n", err=True)

        dg_connection.on(LiveTranscriptionEvents.Transcript, on_message)
        dg_connection.on(LiveTranscriptionEvents.Error, on_error)

        options = LiveOptions(
            model="nova-2",
            punctuate=True,
            language="en-US",
            encoding="linear16",
            channels=1,
            sample_rate=16000,
            endpointing=True,
        )

        await dg_connection.start(options)

        microphone = Microphone(dg_connection.send)
        microphone.start()

        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, signal_handler)

        click.echo("Listening... Press Ctrl+C to stop.")

        await shutdown_event.wait()

        click.echo("Stopping microphone...")
        microphone.finish()

        click.echo("Closing Deepgram connection...")
        await dg_connection.finish()

        click.echo("Shutdown complete.")

    except Exception as e:
        click.echo(f"An error occurred: {e}", err=True)
    finally:
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.remove_signal_handler(sig)


@click.command()
@click.option(
    "--batch-size",
    envvar="BATCH_SIZE",
    help="Size of the batch to send to Deepgram",
    default=10,
)
@click.option("--api-key", envvar="DEEPGRAM_API_KEY", help="Deepgram API Key")
def main(api_key: str, batch_size: int):
    """Run real-time transcription using Deepgram."""
    if not api_key:
        raise click.UsageError(
            "The Deepgram API key is required. Set it using --api-key or the DEEPGRAM_API_KEY environment variable."
        )
    settings = Settings(
        DEEPGRAM_API_KEY=api_key,
        BATCH_SIZE=batch_size,
    )

    transcript_collector = TranscriptCollector(batch_size=settings.BATCH_SIZE)

    asyncio.run(
        get_transcript(
            api_key=settings.DEEPGRAM_API_KEY, transcript_collector=transcript_collector
        )
    )


if __name__ == "__main__":
    main()
