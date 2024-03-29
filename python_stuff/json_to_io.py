#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random
import json

app = Flask(__name__)


@app.route('/')
def output():
	# serve index template
	return render_template('index.html', name='Joe')


@app.route('/receiver', methods=['POST'])
def worker():
    # read json + reply
    data = request.form.to_dict(flat=True)
    result = ''
    print(data)
    for i in data:
        result+=i
    return result


if __name__ == '__main__':
	# run!
	app.run()
