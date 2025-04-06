import socket

# Crear socket TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular socket a localhost y puerto
serverSocket.bind(('localhost', 8080))

# Escuchar conexiones
serverSocket.listen(1)
print("Servidor TCP iniciado en localhost:8080")

while True:
    # Aceptar conexión
    connectionSocket, address = serverSocket.accept()
    print(f"\nConexión aceptada de {address[0]}:{address[1]}")
    
    # Cerrar conexión del cliente
    connectionSocket.close() 