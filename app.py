from flask import Flask
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask_swagger_ui import get_swaggerui_blueprint

# Crear la aplicación Flask
app = Flask(__name__)

# Definir el servicio SOAP
class MiServicio(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def obtener_saludo(ctx, nombre):
        return f"Hola, {nombre}! Bienvenido a tu primer servicio SOAP con Python."

# Configurar la aplicación SOAP de Spyne
soap_app = Application(
    [MiServicio],
    'mi.soap.servicio',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# Configurar la aplicación WSGI
wsgi_app = WsgiApplication(soap_app)

# Configurar Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Aquí es donde tendrás tu archivo Swagger

swagger_ui = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Servicio SOAP con Swagger MATEO CARRASCO"}
)

# Registrar el blueprint de Swagger UI
app.register_blueprint(swagger_ui, url_prefix=SWAGGER_URL)

# Definir una ruta para la documentación Swagger
@app.route('/static/swagger.json')
def swagger_json():
    return app.send_static_file('swagger.json')


# Crear el servidor para ejecutar la aplicación
if __name__ == "__main__":
    from wsgiref.simple_server import make_server

    # Ejecutar el servidor en el puerto 8000
    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Servicio SOAP ejecutándose en http://localhost:8000")
    
    # Ejecutar el servidor de Flask en el puerto 5000 para Swagger
    app.run(port=5000)
    
    server.serve_forever()
