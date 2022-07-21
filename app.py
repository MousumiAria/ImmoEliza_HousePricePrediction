import numpy as np
from flask import Flask,render_template,request,jsonify
import pickle
import json
from predict import prediction

app = Flask(__name__)
 
#route to form to get house details from user
#@app.route('/HouseDetails/', methods = ['POST', 'GET'])
@app.route('/', methods = ['POST', 'GET'])
def inputdata():

    index_pqge="Default.html"
    if request.method == 'GET':
        return render_template(index_pqge)
    if request.method == 'POST':

        #check which button is clicked
        btn_action = request.form['btn_submit'] 

        #f validate then prepare the json data else predict the price
        if btn_action == "Validate":
            jsonReq = createJsonDataFromRequest(request)
            return render_template(index_pqge,json_data = jsonReq)
        else:
            #house_data = request.form['jsonHouse_data'] 
            house_data =  createJsonDataFromRequest(request)

            if house_data != "":
                data = json.loads(house_data)                
                #list = data
                predic_price = prediction.predict(list(data.values()))
                round_price=round(predic_price,2)
                return render_template(index_pqge,price = round_price)
            else:
                error_data = "please validate first"
                return render_template(index_pqge,error = error_data)
          
        
def createJsonDataFromRequest(req):
    """
    get the request form data and create json

    Parameters
    ----------
    request

    Returns
    -------
    json data
    """

    form_data = req.form
    data = {}
   
    data["house_surface"]=  int(form_data['house_surface'])
    data["house_bedroom"]=  int(form_data['house_bedroom'])

    if 'house_attic' in form_data:
      data["house_attic"] =  int(form_data['house_attic'])
    else:
      data["house_attic"] =  0
   
    if 'house_terrace' in form_data:
      data["house_terrace"] =  int(form_data['house_terrace'])
    else:
      data["house_terrace"] =  0
   

    if 'house_swimmingpool' in form_data:
      data["house_swimmingpool"] =  int(form_data['house_swimmingpool'])
    else:
      data["house_swimmingpool"] =  0

    json_data = json.dumps(data)

    return json_data

#app.run(host='localhost', port=5002)
#app.run()