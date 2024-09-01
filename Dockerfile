FROM python:3.12-alpine

WORKDIR /ims

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD ["fastapi","run","app/main.py","--port","80"]