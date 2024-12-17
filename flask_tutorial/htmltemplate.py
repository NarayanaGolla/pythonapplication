from flask import Flask, render_template

htmltemplate = Flask(__name__)

@htmltemplate.route('/')
def home():
    return render_template('index.html')
