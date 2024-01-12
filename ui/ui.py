from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Running on -> '+ os.uname()[1]

app.run(host='0.0.0.0', port=80)