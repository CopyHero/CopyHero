FROM python:3.8-slim

WORKDIR /CopyHero
COPY ./app /CopyHero/app
RUN apt-get update \
    && apt-get install -y gcc python3-dev libgl1-mesa-glx libglib2.0-0\
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /CopyHero
COPY env_template /CopyHero/app/.local.env

RUN pip install -r requirements.txt
RUN pip install paddlepaddle
RUN pip install "paddleocr>=2.0.1"

EXPOSE 8899

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8899"]