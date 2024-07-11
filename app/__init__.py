from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flasgger import Swagger
from dotenv import load_dotenv
from .config import Config

db = SQLAlchemy()
app = Flask(__name__)
    
load_dotenv()
app.config.from_object(Config)
    
db.init_app(app)

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  
            "model_filter": lambda tag: True,  
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/",
    "swagger_ui_bundle_js": "//unpkg.com/swagger-ui-dist/swagger-ui-bundle.js",
    "swagger_ui_standalone_preset_js": "//unpkg.com/swagger-ui-dist/swagger-ui-standalone-preset.js",
    "swagger_ui_css": "//unpkg.com/swagger-ui-dist/swagger-ui.css",
    "swagger_ui_favicon_32": "//path/to/your/favicon-32x32.png",
    "swagger_ui_favicon_16": "//path/to/your/favicon-16x16.png",
    "ui_params": {
        "docExpansion": "none",
        "defaultModelsExpandDepth": -1,
        "layout": "BaseLayout",  
    },
    "docExpansion": "none",
    "operationsSorter": "alpha",
}

swagger_template = {
    "info": {
        "title": "CEP API",
        "description": "API que realiza consultas em outras APIs para retornar endereços com base no CEP informado",
        "version": "1.0.0",
        "contact": {
            "responsibleOrganization": "Richard Fontoura",
            "responsibleDeveloper": "Richard Fontoura",
        },

    },
    "host": "localhost:5000", 
    "basePath": "/",
    "schemes": [
        "http"
    ],
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)

#Rotas
from .routes import routes_cep

#Models
from .models.cep import CEP
    
api = Api(app)

with app.app_context():
    db.create_all()