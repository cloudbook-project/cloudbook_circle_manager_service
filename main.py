from flask import Flask
from flask_restful import Api
import communicationLayer


app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    communicationLayer.app.run(port='5002')