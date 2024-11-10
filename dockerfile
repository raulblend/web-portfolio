FROM python:3.10.12-slim

RUN apt-get update && apt-get install -y unzip curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000 8000

CMD [ "reflex", "run" ]