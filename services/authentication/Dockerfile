FROM python:3.13-slim

WORKDIR /service

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

COPY src .

USER appuser

EXPOSE 8000

CMD ["fastapi", "run", "--host", "0.0.0.0", "application.py"]