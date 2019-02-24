import sys
from flask import Flask, render_template, request, redirect, Response
import random
import json

app = Flask(__name__)

@app.route('/')
# @app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/inpu', methods=['POST'])
def worker():
    # read json + reply
    data = request.form.to_dict(flat=True)
    result = ''
    # print("GOOD")
    print(data)
    # print("GOOD")
    for i in data:
        result += i
    return result
