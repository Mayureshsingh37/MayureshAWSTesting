from flask import Flask # type: ignore
applictaion = Flask(__name__)

@applictaion.route('/')
def hello_world():
    return 'Hello, World!'