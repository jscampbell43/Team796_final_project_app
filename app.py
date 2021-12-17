# Course: CST205
# Title: Nutrition App
# Abstract: This app is for people to search for food products using a general 
# keyword search or a search that includes criteria like "category" "nutrition_grade" etc.
# A list of search results is displayed with the product name and image.
# 
# Authors: James Campbell, Dale Sanchez, Aret Tinoco
# Date: 12/16/21
# Who worked on which functions/classes/files
# James Campbell:
# Initial App setup app.py, result.html, API setup: endpoint, try request, except.
# Got API response displayed as list of picture/image combos.
# Implemented general keyword search, modified class SearchTerms, def store_term, and results route
# Dale Sanchez:
# Created the initial search bar and got the basic search working. Worked with James to better fine tune
# the search bar when it wasn't working properly. Worked on routes and Flask Forms and got them set up and
# working for the creation of the search bar.  
# Aret Tinoco:
# 
# 
# Sources cited: API used: Open Food Facts - https://world.openfoodfacts.org/
# For Open Food Facts API documentation: https://world.openfoodfacts.org/data
#
# Github Link: https://github.com/jscampbell43/Team796_final_project_app


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

# Class connected to Flaskform
class Search_Terms(FlaskForm):
  searchBarKeyword = StringField('General Search', validators=[DataRequired()])
  searchBar = StringField('Category')#, validators=[DataRequired()])
  searchBar2 = StringField('Nutrition Grade')#, validators=[DataRequired()])

# List for storing dictionary of returned search terms
searchTerms = []

# Function to take form input terms and add them to dictionary and add to searchTerms list
def store_term(newKeyword, newTerm, newTerm2):
  searchTerms.append(dict(keyword = newKeyword, term = newTerm, term2 = newTerm2))

@app.route('/', methods = ('GET', 'POST'))
def home():
  # Form submission logic
  form = Search_Terms()
  if form.validate_on_submit():
    # clear dictionary here
    searchTerms.clear()
    # store new terms recieved from the form to dictionary and add to searchTerms list
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
  # Beginning of URL for call to Open Food Facts API
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
    print('please try again, in route /results')
  return render_template('result.html', my_data = data)