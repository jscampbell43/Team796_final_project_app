# comment test

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
  searchBarKeyword = StringField('General Search', validators=[DataRequired()])
  searchBar = StringField('Category')#, validators=[DataRequired()])
  searchBar2 = StringField('Nutrition Grade')#, validators=[DataRequired()])


searchTerms = []

def store_term(newKeyword, newTerm, newTerm2):
  searchTerms.append(dict(keyword = newKeyword, term = newTerm, term2 = newTerm2))

@app.route('/', methods = ('GET', 'POST'))
def home():
  # clear dictionary here:
  form = Search_Terms()
  if form.validate_on_submit():
    searchTerms.clear()
    store_term(form.searchBarKeyword.data, form.searchBar.data, form.searchBar2.data)
    return redirect('/results')
  return render_template('index.html', form = form)

@app.route('/results')
def result():
  pprint(searchTerms)
  # Get search term and criteria from searchTerms dictionary 
  tempKeyword = searchTerms[0]['keyword']
  temp = searchTerms[0]['term']
  temp2 = searchTerms[0]['term2']
  print(tempKeyword)
  print(temp)
  print(temp2)
  # Beggining of URL
  endpoint = 'https://us.openfoodfacts.org/cgi/search.pl?search_terms='
  # Add general search keyword
  endpoint = endpoint + str(tempKeyword)
  # Set search_simple and action
  endpoint = endpoint + '&search_simple=1&action=process'
  # If Category is not blank add category criteria
  if temp != '':
    endpoint = endpoint + '&tagtype_0=categories&tag_contains_0=contains&tag_0='
    endpoint = endpoint + str(temp) 
  # If Nutrition Grade is not blank add nutrition_grades
  if temp2 != '':
     endpoint = endpoint + '&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1='
     endpoint = endpoint + str(temp2)
  # Ending of URL
  endpoint = endpoint + '&fields=product_name,image_url&json=1'  
  print(endpoint)
  # API Call
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