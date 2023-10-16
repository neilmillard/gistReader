FROM python:3.10

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY Makefile Makefile

COPY . .
COPY ./src /code/src
EXPOSE 5000

CMD [ "python", "-m", "app" ]
