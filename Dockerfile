FROM python:2.7.15-alpine3.8

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]