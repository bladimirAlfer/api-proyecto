# api-proyecto

## Dockerfiles

### Dockerfile y comandos
```
#correr el back en localhost
uvicorn main:app --reload


#Modificar nginx.conf


#Dockerfile para API de Medicos
docker exec -it frontend_c /bin/sh

apk update
apk add nano

nano /etc/nginx/conf.d/default.conf

#En  default.conf, cambiar el puerto del front:

server {
    listen       8000;
    listen  [::]:8000;
    server_name  localhost;

    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    #error_page  404              /404.html;

nginx -s reload


FROM python:3.10-slim
WORKDIR /programas/api-medicos
RUN pip install fastapi pydantic mysql-connector-python passlib python-jose uvicorn
COPY . .
EXPOSE 8010
CMD ["uvicorn", "app_medicos:app", "--host", "0.0.0.0", "--port", "8010"]

#Dockerfile para API de Citas

FROM python:3.10-slim
WORKDIR /programas/api-citas-medicas
RUN pip install fastapi pydantic mysql-connector-python passlib python-jose uvicorn
COPY . .
EXPOSE 8011
CMD ["uvicorn", "app_citas_medicas:app", "--host", "0.0.0.0", "--port", "8011"]

#Dockerfile para API de Pacientes

FROM python:3.10-slim
WORKDIR /programas/api-pacientes
RUN pip install fastapi pydantic mysql-connector-python passlib python-jose uvicorn
COPY . .
EXPOSE 8012
CMD ["uvicorn", "app_pacientes:app", "--host", "0.0.0.0", "--port", "8012"]

#Dockerfile para Frontend

FROM nginx:alpine
COPY .  /usr/share/nginx/html
EXPOSE 8000



#Entrar a Docker
docker login -u bladimiralf

#Construcción de imágenes

docker build -t frontend .
docker build -t api-medicos .
docker build -t api-citas-medicas .
docker build -t api-pacientes .


#Etiquetado y subida de imágenes a Docker Hub

docker tag frontend bladimiralf/frontend
docker push bladimiralf/frontend

docker tag api-medicos bladimiralf/api-medicos
docker push bladimiralf/api-medicos

docker tag api-citas-medicas bladimiralf/api-citas-medicas
docker push bladimiralf/api-citas-medicas

docker tag api-pacientes bladimiralf/api-pacientes
docker push bladimiralf/api-pacientes


#Ejecucion de contenedores

docker run -d --rm --name frontend_c -p 8000:8000 bladimiralf/frontend
docker run -d --rm --name api-medicos_c -p 8010:8010 bladimiralf/api-medicos
docker run -d --rm --name api-citas-medicas_c -p 8011:8011 bladimiralf/api-citas-medicas
docker run -d --rm --name api-pacientes_c -p 8012:8012 bladimiralf/api-pacientes
