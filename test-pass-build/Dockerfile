# ---------- Stage 1: Testing ----------
FROM python:3.11-slim AS test

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest

COPY . .
# Run tests
RUN pytest --maxfail=1 --disable-warnings -q


# ---------- Stage 2: Build final API ----------
FROM python:3.11-slim AS final

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app

EXPOSE 8000
CMD ["python", "app/main.py"]
