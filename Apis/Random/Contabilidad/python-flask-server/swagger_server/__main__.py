#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'API para la gestion de la contabilidad de la universidad, profesores y alumnos, ademas de los salrios, precios de las instalciones, matriulas, etc.'})
    app.run(port=8080)
