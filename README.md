# api-proyecto

## Dockerfiles

### Dockerfile para API de Médicos
```Dockerfile
FROM python:3.10-slim
WORKDIR /programas/api-medicos
RUN pip install fastapi pydantic mysql-connector-python passlib python-jose uvicorn
COPY . .
EXPOSE 8010
CMD ["uvicorn", "app_registro:app", "--host", "0.0.0.0", "--port", "8010"]

FROM python:3.10-slim
WORKDIR /programas/api-citas-medicas
RUN pip install fastapi pydantic mysql-connector-python passlib python-jose uvicorn
COPY . .
EXPOSE 8011
CMD ["uvicorn", "app_registro:app", "--host", "0.0.0.0", "--port", "8011"]

FROM python:3.10-slim
WORKDIR /programas/api-pacientes
RUN pip install fastapi pydantic mysql-connector-python passlib python-jose uvicorn
COPY . .
EXPOSE 8012
CMD ["uvicorn", "app_registro:app", "--host", "0.0.0.0", "--port", "8012"]

docker login -u bladimiralf

#Etiquetado y subida de imágenes a Docker Hub

docker build -t frontend .
docker build -t api-medicos .
docker build -t api-citas-medicas .
docker build -t api-pacientes .

#Ejecucion de contenedores

docker run -d --rm --name api-medicos_c -p 8010:8010 bladimiralf/api-medicos
docker run -d --rm --name api-citas-medicas_c -p 8011:8011 bladimiralf/api-citas-medicas
docker run -d --rm --name api-pacientes_c -p 8012:8012 bladimiralf/api-pacientes
