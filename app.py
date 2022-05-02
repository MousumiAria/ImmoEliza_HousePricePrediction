import numpy as np
from flask import Flask,render_template,request

app = Flask(__name__)
 
#route to form to get house details from user
@app.route('/HouseDetails/')
def inputdata():
    return render_template('HouseDetails.html')

#route to form to show predicted price for the required house
@app.route('/result/', methods = ['POST', 'GET'])
def output():
    if request.method == 'GET':
        return f"The URL /output is accessed directly. Try going to '/input' to submit form"
    if request.method == 'POST':
        form_data = request.form
        
    #call the model to predict the price based on form data
    calcprice = "345"

    #return render_template('data.html',result=result)
    return render_template('result.html',price=calcprice)
 

app.run(host='localhost', port=5000)
