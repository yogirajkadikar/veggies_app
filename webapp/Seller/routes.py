from flask import render_template
from webapp import app

@app.route('/')
def index():
    return render_template('Seller/index.html')