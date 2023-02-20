FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./.env /code/.env
COPY ./main.py /code/main.py
COPY ./app /code/app

RUN apt-get update && apt-get install -y libzbar0
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "main.py"]
