import os
from flask import Flask
from models import setup_db
from flask_cors import CORS
import os

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello" 
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "STOOOPID UR SO STOOOPID, CHARLOTTE UR SO STOOOOOOOOOPID"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
