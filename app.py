from flask import Flask, render_template, redirect, url_for, request
from db import data
from img_upload import handle_file_upload

app = Flask(__name__)


@app.route('/')
def get_all_plants():
    return render_template('plants.html', plants=data)
