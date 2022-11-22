import flask
from flask import Flask, jsonify, request
import datetime
import rest

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
rest.get_access(rest.PARAMS)

# Route for seeing a data
@app.route('/get_candidats')
def get_data():
    result = []
    response = rest.get_all_candidatures()
    for c in response:
        obj = {'id': c['Id'],
               'firstName': c['First_Name__c'],'LastName': c['Last_Name__c'],'YearOfExperience': c['Year_Of_Experience__c']}
        result.append(obj)
    return jsonify(result)


# Route for adding data
@app.route('/add_candidat',methods=['POST'])
def add_data():
    _req = request.get_json()
    rest.create_candidature(_req['prenom'],_req['nom'],_req['year_of_experience'])
    return 'inserted',200


# Running app
if __name__ == '__main__':
    app.run(debug=True)

