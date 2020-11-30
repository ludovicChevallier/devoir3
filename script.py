#!/usr/bin/env python
#flask crée un site web
from flask import Flask
#crée une instance de la class flask
app = Flask(__name__)
#url de base de mon site web ex wikipedia/napoléon
@app.route('/hi')
#quand on cliqué sur l'url va afficher la fonction hello world
def hello_world():
    return 'Hello World!'
    #définis le port et l'adresse ip du site web
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)