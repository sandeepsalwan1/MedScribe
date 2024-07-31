FROM python:3.12

ARG env

RUN python -m pip install --upgrade pip
RUN pip install poetry

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache



COPY poetry.lock pyproject.toml ./


RUN poetry install
RUN rm -rf $POETRY_CACHE_DIR

COPY ./ ./

RUN poetry install


CMD ["poetry", "run", "fastapi", "run", "main.py", "--port", "8000"]

# CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


EXPOSE 8000