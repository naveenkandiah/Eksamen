# Produckt Service

from flask import Flask
from flask-restful import Resource, Api

app = FLask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'Product': ['RedBull'
                        'Cult'
                        'RockStar'
                        'X-Ray']
        }

api.add_resouce(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=true)
