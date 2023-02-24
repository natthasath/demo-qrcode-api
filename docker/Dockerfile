FROM python:3.9

WORKDIR /code

COPY ./poetry.lock /code/poetry.lock
COPY ./pyproject.toml /code/pyproject.toml
COPY ./.env /code/.env
COPY ./main.py /code/main.py
COPY ./app /code/app

RUN apt-get update && apt-get install -y libzbar0
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["python", "main.py"]
