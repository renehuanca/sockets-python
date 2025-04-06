# Taller de Programación con Sockets en Python

Este repositorio contiene tres programas que demuestran el uso de sockets en Python:

## 1. Cliente TCP (cliente_tcp.py)

Este programa establece una conexión TCP con un host remoto y muestra información sobre la conexión.

```bash
python servidor_tcp.py
```

luego ejecutar el cliente:

```bash
python cliente_tcp.py
```

El programa se conecta a localhost en el puerto 8080.

## 2. Cliente HTTP (cliente_http.py)

Este programa realiza una petición HTTP a un servidor web y muestra las cabeceras y el contenido HTML de la respuesta.

```bash
python cliente_http.py www.fcpn.edu.bo
```

El programa se conecta a www.fcpn.edu.bo.

## 3. Contador de Vocales (cliente-servidor UDP)

### Servidor (servidor_vocales.py)

El servidor UDP que cuenta vocales en el texto recibido.

```bash
python servidor_vocales.py
```

### Cliente (cliente_vocales.py)

El cliente UDP que envía texto al servidor para contar vocales.

```bash
python cliente_vocales.py
```

El cliente envía el texto "Hola Mundo" al servidor.

## Requisitos

- Python 3.x
- Módulo socket (incluido en la biblioteca estándar de Python)

## Notas

- Todos los programas utilizan los módulos de socket, sys, ssl de Python
- El servidor de vocales debe estar ejecutándose antes de usar el cliente
- Para terminar el servidor de vocales, presione Ctrl+C 