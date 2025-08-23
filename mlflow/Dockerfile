# Dockerfile
FROM python:3.12

WORKDIR /app



RUN pip install --no-cache-dir psycopg2-binary mlflow

CMD ["mlflow", "server", "--host", "0.0.0.0", "--port", "8080","--backend-store-uri", "postgresql://mlflow:mlflow@postgres/mlflow_db", "--default-artifact-root", "/mlflow/artifacts"]
