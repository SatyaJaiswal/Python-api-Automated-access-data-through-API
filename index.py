from flask import Flask, request, jsonify, abort
from flask_restful import Resource, Api
import pymongo
import json

app = Flask(__name__)
api = Api(app)

# Connect to the MongoDB server running locally. You can customize the connection URL as needed.
client = pymongo.MongoClient("mongodb://localhost:27017")

# Select the database and collection
db = client["patient"]
collection = db["patient_database"]

def load_admin_credentials():
    try:
        with open('admin_credentials.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

admin_credentials = load_admin_credentials()

class AdminLogin(Resource):
    def post(self):
        auth_username = request.json.get('username')
        auth_password = request.json.get('password')

        if auth_username == admin_credentials.get('admin_username') and auth_password == admin_credentials.get('admin_password'):
            return jsonify({"message": "Admin logged in successfully"})
        else:
            abort(401)  # Unauthorized

class PatientInfo(Resource):
    def get(self):
        auth_username = request.headers.get('Username')
        auth_password = request.headers.get('Password')

        if auth_username == admin_credentials.get('admin_username') and auth_password == admin_credentials.get('admin_password'):
            name = request.args.get('name')  # Get the name as a query parameter
            if name:
                # Search for the document with the specified name
                result = collection.find_one({"name": name})

                if result:
                    # Extract and return the name, address, and mobile number from the document
                    return jsonify({
                        "Name": result.get("name"),
                        "Address": result.get("Address"),
                        "Mobile Number": result.get("mobile_number")
                    })
                else:
                    return jsonify({"message": "Name not found"}, 404)
            else:
                return jsonify({"message": "Please provide a name in the query parameter"}, 400)
        else:
            abort(401)  # Unauthorized

api.add_resource(AdminLogin, '/admin/login')
api.add_resource(PatientInfo, '/get_contact_info')

if __name__ == '__main__':
    app.run()
