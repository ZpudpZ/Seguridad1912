from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import hashlib

# Definir una clave más segura usando SHA-256 para obtener una clave de 32 bytes (AES-256)
def generate_key(password: str):
    return hashlib.sha256(password.encode()).digest()  # Genera una clave de 32 bytes

ENCRYPTED_FOLDER = 'encrypted_files/'

# Encriptar el archivo
def encrypt_file(file, password: str):
    file_content = file.read()
    key = generate_key(password)  # Genera la clave segura a partir de la contraseña
    cipher = AES.new(key, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(file_content, AES.block_size))

    filename_safe = file.filename.replace(" ", "_")  # Reemplazar los espacios por guiones bajos
    encrypted_file_path = os.path.join(ENCRYPTED_FOLDER, f'encrypted_{filename_safe}')

    # Guardamos IV + datos cifrados
    with open(encrypted_file_path, 'wb') as f:
        f.write(cipher.iv + encrypted_data)

    print(f"Archivo encriptado guardado en: {encrypted_file_path}")  # Mensaje de depuración

    return encrypted_file_path

# Desencriptar el archivo
def decrypt_file(filename, password: str):
    filename_safe = filename.replace(" ", "_")  # Reemplazar los espacios por guiones bajos
    encrypted_file_path = os.path.join(ENCRYPTED_FOLDER, f'encrypted_{filename_safe}')

    # Verificar si el archivo existe
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"El archivo {encrypted_file_path} no existe.")

    print(f"Archivo encontrado para desencriptar: {encrypted_file_path}")  # Mensaje de depuración

    with open(encrypted_file_path, 'rb') as f:
        iv = f.read(16)  # Leer el IV (tamaño de bloque de AES)
        encrypted_data = f.read()

    key = generate_key(password)  # Genera la misma clave para desencriptar
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Ruta del archivo desencriptado
    decrypted_file_path = f'decrypted_{filename_safe}'

    # Guardamos los datos desencriptados
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)

    return decrypted_file_path

