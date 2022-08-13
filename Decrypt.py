from cryptography.fernet import Fernet
import os


def generarkey():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)


def retornarkey():
    return open("key.key", "rb").read()


def decrypt(items, key):
    i = Fernet(key)
    for x in items:
        with open(x, "rb") as file:
            file_data=file.read()
        data = i.decrypt(file_data)

        with open(x,"wb") as file:
            file.write(data)


if __name__ == "__main__":
    archivos = 'C:\\Users\\erick\\Desktop\\Ataque\\Primera prueba'
    os.remove(archivos+"\\"+"readme.txt")
    items = os.listdir(archivos)
    archivos_2 = [archivos+"\\"+ x for x in items]


key = retornarkey()

decrypt(archivos_2, key)