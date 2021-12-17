# Title: 
# Abstract: 
# Class: CST 205-01
# Authors: James Campbell, Dale Saanchez, and Aret Tinoco
# Date: 12/11/21

from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests, json
from pprint import pprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'team796'
bootstrap = Bootstrap(app)


my_key = 'D8FJrAVDcE5RHJ29uwD5lRftLXMDO6Tw3iGnj19V'

payload = {
  'api_key': my_key,
  'start_date': '2017-03-09',
  'end_date': '2017-03-11'
}
endpoint = 'https://us.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=meat&fields=product_name,image_url&json=1'
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

class Search_Terms(FlaskForm):
  searchBar = StringField('Search Term', validators=[DataRequired()])
  searchBar2 = StringField('Search Term 2', validators=[DataRequired()])


searchTerms = []

def store_term(newTerm, newTerm2):
  searchTerms.append(dict(term = newTerm, term2 = newTerm2))

@app.route('/', methods = ('GET', 'POST'))
def home():
  # clear dictionary here:
  searchTerms = []
  form = Search_Terms()
  if form.validate_on_submit():
    store_term(form.searchBar.data, form.searchBar2.data)
    return redirect('/results')
  return render_template('index.html', form = form)

@app.route('/results')
def result():
  temp = searchTerms[0]['term']
  temp2 = searchTerms[0]['term2']
  print(temp)
  print(temp2)
  endpoint = 'https://us.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0='
  #meat&fields=product_name,image_url&json=1'
  endpoint = endpoint + str(temp)  
  endpoint = endpoint + '&tagtype_1=brand&tag_contains_1=contains&tag_1='
  endpoint = endpoint + str(temp2)
  endpoint = endpoint + '&fields=product_name,image_url&json=1'  
  print(endpoint)
  try:
    r = requests.get(endpoint, params=payload)
    data = r.json()
    pprint(data[0:10])
  except:
    print('please try again, in result.route')
  return render_template('result.html', my_data = data)






# Failed attempt at search implementation  
# @app.route('/form')
# def form():
#     return render_template('form.html')
 
# @app.route('/data/', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         #form_data = request.form
#         search = request.form.Search
#         return render_template('data.html',form_data = search)