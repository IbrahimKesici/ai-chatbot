FROM python:3.9-alpine

WORKDIR /usr/src/ai-chatbot
COPY ./requirements.txt ./
RUN apk update && \ 
    apk add build-base gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev && \
    pip3 install --no-cache-dir -r requirements.txt && \
    python3 -m nltk.downloader punkt

COPY . .
CMD ["python", "./ai_chatbot/main.py"]