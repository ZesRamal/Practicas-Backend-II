# Docker Proxy
<b>Elaborado por:</b> Ramos Leal Cesar Francisco

Ésta práctica consiste en un Docker con Nginx con el puerto 80 con Python instalado dentro del contenedor, y un proxy para responder por enpoint /pagina para resolver el puerto 5000 del FLASK retornando un "hola mundo".

Para ejecutarlo se abre una terminal en la ubicación del proyecto y ejecutar lo siguiente:

```bash
# Construir la imagen
docker-compose build
# Ejecutar el contenedor
docker-compose up
```
