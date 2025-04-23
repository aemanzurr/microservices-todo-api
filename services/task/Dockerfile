FROM python:3.13-slim

WORKDIR /service

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    gcc \
    libssl-dev \
    curl\
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

USER appuser

EXPOSE 8001

CMD ["fastapi", "run", "src/application.py", "--host", "0.0.0.0", "--port", "8001"]