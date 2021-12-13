FROM python:3.11-rc-alpine

WORKDIR /usr/src/ai-bot-app
COPY ./requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "./main.py"]