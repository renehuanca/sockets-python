import socket

HOST = 'localhost'
PUERTO_SERVIDOR = 8080

# Crear socket TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor remoto
clientSocket.connect((HOST, PUERTO_SERVIDOR))

# Obtener información del socket remoto
ip_remota, puerto_remoto = clientSocket.getpeername() # socket remoto par

# Obtener información local
ip_local, puerto_local = clientSocket.getsockname() # socket local

# Mostrar información
print(f"Host remoto: {ip_remota}")
print(f"Puerto remoto: {puerto_remoto}")
print(f"IP local: {ip_local}")
print(f"Puerto local: {puerto_local}")

clientSocket.close() 