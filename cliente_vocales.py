import socket

# Valores constantes
TEXTO = "Hola Mundo"
HOST = 'localhost'
PUERTO = 5000

# Crear socket UDP
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar mensaje al servidor
cliente.sendto(TEXTO.encode('utf-8'), (HOST, PUERTO))

# Recibir respuesta
respuesta, _ = cliente.recvfrom(1024)
print("\nRespuesta del servidor:")
print(respuesta.decode('utf-8'))

cliente.close() 