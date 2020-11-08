import flask
import numpy as np
from flask import Flask, request, jsonify, render_template
import image_processing as ip
import pickle
import os
import sys
from tensorflow import keras
app = flask.Flask(__name__, template_folder='templates',static_url_path = "/static", static_folder = "static")

global model
model = keras.models.load_model('my_model')

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return(render_template('main.html'))
    if flask.request.method == 'POST':
        image_name = request.form['filename']
        x_value = ip.get_x_value(image_name)
        ans = model.predict_classes(x_value)
        if ans == 1:
            ans ='an "Original" '
            audio_file_name = 'orig_audio.mp3'
        else:
            ans = 'a "Fake"'
            audio_file_name = 'fake_audio.mp3'
        #save audio file
        return(flask.render_template('result.html', answer = ans, load_image = image_name, audio_file = audio_file_name ))

@app.route('/about', methods=['GET', 'POST'])
def about():
    return(render_template('about.html'))

@app.route('/result', methods=['GET'])
def result():
    return(render_template('result.html'))

if __name__ == '__main__':
    app.run()