import socket

def contar_vocales(texto):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vocales:
            contador += 1
    return contador

HOST = 'localhost'
PUERTO = 5000

# Crear socket UDP
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular socket a todas las interfaces y puerto
servidor.bind((HOST, PUERTO))
print("Servidor UDP iniciado en puerto 5000")

while True:
    # Recibir datos
    datos, direccion = servidor.recvfrom(1024) # 1024 bytes
    texto = datos.decode('utf-8')
    
    # Contar vocales
    num_vocales = contar_vocales(texto)
    
    # Preparar respuesta
    respuesta = f"Vocales encontradas: {num_vocales}\n"
    respuesta += f"Dirección del cliente: {direccion[0]}:{direccion[1]}"
    
    # Enviar respuesta
    servidor.sendto(respuesta.encode('utf-8'), direccion)
    
servidor.close() 