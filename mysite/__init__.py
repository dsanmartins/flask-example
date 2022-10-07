import os

from flask import Flask
from . import db
from . import auth

# función de factoría de la aplicación
def create_app(test_config=None):
    
    #Crea una instancia de la clase Flask
    app = Flask(__name__, instance_relative_config=True)
    
    # Configuraciones que la aplicación usa (mantener lso datos resguardados
    # la ruta donde se guardará la base de datos sqlite)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'biblioteca.sqlite'),
    )
    
    db.init_app(app)
    app.register_blueprint(auth.bp)

    if test_config is None:
        # sobreescribe la configuración por defecto con valores
        # tomados desde config.py. 
        app.config.from_pyfile('config.py', silent=True)
    else:
        # para correr los tests
        app.config.from_mapping(test_config)

    # asegura que el directorio de la instancia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # una página que retorna hello!
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

