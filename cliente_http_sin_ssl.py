import socket
import sys

# Obtener argumento url
# [1] ya que el primer argumento es el nombre del script
# python ya usa el un dns cuando se le pasa un dominio
HOST = sys.argv[1] 
SERVER_PORT = 80  # Puerto HTTP

# Crear socket TCP
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor HTTP
cliente.connect((HOST, SERVER_PORT))

# Construir y enviar petición HTTP
peticion = "GET / HTTP/1.1\r\n" # HTTP requiere explícitamente \r\n
peticion += f"Host: {HOST}\r\n"
peticion += "Connection: close\r\n" # Cerrar la conexión después de la respuesta
peticion += "\r\n"

cliente.send(peticion.encode()) # Convertir la petición a bytes

# Recibir respuesta
respuesta = b"" # Inicializar respuesta como bytes
while True:
    datos = cliente.recv(4096) # Buffer de 4096 bytes
    if not datos:
        break
    respuesta += datos # Concatenar datos recibidos

# Decodificar y mostrar respuesta
respuesta_texto = respuesta.decode('utf-8', errors='ignore')

# Separar cabeceras y cuerpo
cabeceras, cuerpo = respuesta_texto.split('\r\n\r\n', 1)

print("\nCabeceras HTTP:")
print(cabeceras)
print("\nContenido HTML:")
print(cuerpo)

cliente.close() 