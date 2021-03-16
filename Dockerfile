# For the good of all beings.

FROM python:3.8-alpine

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ecorpse ecorpse

WORKDIR /ecorpse

EXPOSE 5000
