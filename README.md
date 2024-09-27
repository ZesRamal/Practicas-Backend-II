# ChatCMD

Elaborado por: Ramos Leal Cesar Francisco

Ésta práctica consiste en un chat de terminal entre instancias de clientes conectados a una instacia de servidor para compartir mensajes entre clientes. 
Además presenta la posibilidad de introducir el comando "lsFiles" para obtener la lista de archivos en el directorio de "Files" del servidor y el comando "get [nombre de archivo]" para transferir un archivo del servidor al cliente.

Para ejecutarlo se debe de correr el archivo de server-socket.py y un máximo de 10 instancias del archivo cliente-socket.py

### Implementaciones pendientes:
- Permitir solo el envío de archivos de texto.
- Implementar indicador de progreso de envío de archivo.
- Comando de ayuda.
- Indicar el límite de peso de archivo a descargar.
