#Dockerfile para Frontend

FROM nginx:alpine
RUN apk update && apk add nano
COPY default.conf /etc/nginx/conf.d/default.conf

# Copiar los archivos de tu aplicación frontend al directorio de Nginx
COPY . /usr/share/nginx/html
EXPOSE 8000

# Comando para ejecutar Nginx en el contenedor
CMD ["nginx", "-g", "daemon off;"]
