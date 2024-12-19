from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')  # Carga las configuraciones desde config.py

    # Configuración de las rutas
    from .routes import main
    app.register_blueprint(main)

    return app
