from flask import Blueprint, request, send_file, render_template
from .file_manager import encrypt_file, decrypt_file

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    # Verificar si el archivo y la contraseña están presentes en la solicitud
    if 'file' not in request.files or 'password' not in request.form:
        return 'Archivo o contraseña no proporcionados', 400

    file = request.files['file']
    password = request.form['password']  # Obtenemos la contraseña del formulario

    if file.filename == '':
        return 'No se seleccionó ningún archivo', 400

    filename = file.filename

    try:
        # Usamos la contraseña para generar la clave y encriptar el archivo
        encrypted_file_path = encrypt_file(file, password)
        return f'Archivo {filename} subido y encriptado con éxito: {encrypted_file_path}'
    except Exception as e:
        return f'Error al encriptar el archivo: {str(e)}', 500

@main.route('/download', methods=['POST'])  # Cambié a POST
def download_file():
    # Verificar si el nombre del archivo y la contraseña están presentes en la solicitud
    if 'filename' not in request.form or 'password' not in request.form:
        return 'Nombre de archivo o contraseña no proporcionados', 400

    filename = request.form['filename']  # Obtener el nombre del archivo desde el formulario
    password = request.form['password']  # Obtener la contraseña del formulario

    try:
        # Llamar a la función de desencriptación con el nombre del archivo y la contraseña
        decrypted_file_path = decrypt_file(filename, password)

        # Devolver el archivo desencriptado
        return send_file(decrypted_file_path, as_attachment=True)
    except Exception as e:
        return f'Error al desencriptar el archivo: {str(e)}', 500
