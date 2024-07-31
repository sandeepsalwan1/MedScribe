import speech_recognition as sr

def transcribe_speech():
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Capture microphone input
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # Adjust the recognizer sensitivity to ambient noise
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Microphone calibrated. Please speak now.")

        # Listen to the first phrase and extract it into audio data
        audio_data = recognizer.listen(source)

        print("Recognizing...")

        # Recognize speech using Google Web Speech API
        try:
            # Recognize the speech in the audio data
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))

if __name__ == "__main__":
    transcribe_speech()

