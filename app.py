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

# When creating a search you can add as many tags as you want seperated by "&"
# It will look something like this for one tag: 
# tagtype_0=categories&tag_contains_0=contains&tag_0=meats
# tagtype_0=categories&tag_contains_0=contains&tag_0=meat&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1=A

# This is with a second tag added


# tagtype_0= 
# Set tagtype_0 to one of the following:
# brands, categories, packaging,labels,origins, manufacturing_places, 
# emb_codes, purchase_places, stores, countries, additives, allergens, 
# traces, nutrition_grades, states, contains, does_not_contain

#tag_contains_0=contains 
# I think this always has to be the same

#tag_0=cereals
#tag_0 is where the actual search term will be entered.

# This is how an API call is composed the "us." at the beginning signifies that it will be us products only.
endpoint = 'https://us.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=cereals&fields=product_name,image_url&json=1'
# endpoint = 'https://us.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=meat&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1=A&additives=without&ingredients_from_palm_oil=without&json=1'



try:
  r = requests.get(endpoint, params=payload)
  data = r.json()
  pprint(data[0:10])
except:
  print('please try again')


# # Ignore this just a place holder for whatever we are passing
# my_info = {
#   'days': ['sun', 'mon', 'tues'],
#   'flavors': ['sweet', 'sour'],
#   'colors': ['blue', 'green', 'brown']
# }

@app.route('/')
def home():
  return render_template('index.html', my_data = data)