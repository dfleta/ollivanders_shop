from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_cors import CORS

app=Flask(__name__)

@app.route('/')
def index():
    # return "Welcome to Olivanders Shop"

    data = {
            'titulo': 'Index',
            'bienvenida':'!Saludos!'

            }
    return render_template('index.html',data=data) 
if __name__ == '__main__':
    app.run(debug=True, port=5000)