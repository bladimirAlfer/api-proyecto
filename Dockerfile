# Usa una imagen base de Python
FROM python:3.10-slim
WORKDIR /programas/api-proyecto
RUN pip install fastapi pydantic mysql-connector-python passlib python-jose uvicorn
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app_medicos:app", "--host", "0.0.0.0", "--port", "8000"]
