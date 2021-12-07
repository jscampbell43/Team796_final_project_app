from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests, json
from pprint import pprint

app = Flask(__name__)
bootstrap = Bootstrap(app)


my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'

payload = {
  'api_key': my_key,
  'start_date': '2017-03-09',
  'end_date': '2017-03-11'
}
endpoint = 'https://world.openfoodfacts.org/api/v0/product/737628064502.json'
try:
  r = requests.get(endpoint, params=payload)
  data = r.json()
  pprint(data[0:10])
except:
  print('please try again')


# Ignore this just a place holder for whatever we are passing
my_info = {
  'days': ['sun', 'mon', 'tues'],
  'flavors': ['sweet', 'sour'],
  'colors': ['blue', 'green', 'brown']
}

@app.route('/')
def home():
  return render_template('index.html', my_data = data)