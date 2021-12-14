# input = "p"

#  #include in search
#  def include(input):
#      #match with the search results or something?
#      results = "penauts"
#      return True if input in results else False

# filtered = filter(include, input)

# #print the results??

# #exlude side?
#  def exclude(input):
#      #match with the search results or something?
#      results = "penauts"
#      return False if input in results else True

# filtered = filter(include, input)

#NEW PLAN
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('filter.html')