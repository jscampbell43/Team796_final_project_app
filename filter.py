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
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # print(request.form.getlist('mycheckbox')) #prints the number selected in powershell
        # if document.getElementById('mycheckbox') == '1': //useless
#NOTE TO SELF: NAME IN CHEBCKBX INDEX IS WHAT IS INSERTED BELOW TO SEARCH FOR THE DESIRED RESULT
        if request.form.get('1'):
            return 'unoooooooo'
        # return 'Done' 
        elif request.form.get('2'):
            return 'dossssssssssssss'
        elif request.form.get('3'):
            return 'tressssssssssss'
    return render_template('filter.html')