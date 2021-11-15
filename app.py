from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Ignore this just a place holder for whatever we are passing
my_info = {
  'days': ['sun', 'mon', 'tues'],
  'flavors': ['sweet', 'sour'],
  'colors': ['blue', 'green', 'brown']
}

@app.route('/')
def home():
  return render_template('index.html', my_data = my_info)