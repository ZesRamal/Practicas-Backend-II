# Docker PostgreSQL

Ésta práctica consiste en generar un Docker, abrir su puerto, generar la base de datos encontrada en el Classroom, e introducir información a ésta última.

El puerto abierto es el default de postgres 5432.

En el docker-compose en 'enviroment' se pueden cambiar los valores de las variables según la preferencia del usuario, contraseña y nombre de base de datos.

Para ejecutarlo se abre uno terminal en la ubicación del proyecto y ejecutar lo siguiente:

```bash
# Construir la imagen
docker-compose build
# Ejecutar el contenedor
docker-compose up
```
