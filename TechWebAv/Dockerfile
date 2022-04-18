# syntax=docker/dockerfile:1
FROM python:2.7.18-alpine
WORKDIR /
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN apk add build-base
RUN python -m pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run", "--host","0.0.0.0"]
