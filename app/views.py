from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Phyllis'}
    return render_template('index.html', title='Jackson',user=user)
