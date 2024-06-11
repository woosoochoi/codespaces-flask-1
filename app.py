from flask import Flask, render_template, redirect, url_for, request
from db import data

app = Flask(__name__)


@app.route('/')
def get_all_plants():
    return render_template('plants.html', plants=data)

def add_plant():
    return render_template('add_plant.html
                           ')