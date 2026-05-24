import os
from flask import Flask, request, jsonify, send_from_directory
import util

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
client_dir = os.path.join(base_dir, 'client')
app = Flask(__name__, static_folder=client_dir, static_url_path='')

@app.route('/')
def home():
    return send_from_directory(client_dir, 'app.html')


@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/api/predict_home_price', methods=['GET','POST'])##check
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response = jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add('Access-Control-Allow-Origin','*')

    return response

if __name__=="__main__":
    print("starting python flask server")
    util.load_saved_artifacts()
    app.run()

