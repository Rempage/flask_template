from . import wap
from flask import render_template

@wap.route('/')
def index():
    return render_template('wap/index.html')