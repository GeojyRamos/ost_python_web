from flask import Flask
app = Flask("Meu app")

@app.route('/')
def hello():
    return "Hello World"