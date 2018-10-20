import http.client
import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
import uuid

app = Flask(__name__)
api = Api(app)
conn = http.client.HTTPSConnection("sandbox.apihub.citi.com")
token = "AAIkN2E3MzM3NTktYzE4Mi00NDNkLTkzZjgtNmU2MDdkOTZiOWMxw50nWOvzDp6U08HXLS5s6Dz_6TK8HuFFPIwZ9A3epRwuy6y_x7qpnVQcwtu9sFIrBt5RuQU3U5JJ3y9DGakhoqrArJ4aS2LBdWMwpdbk-BgmACA83mZllkWkcaZMi8ekeuSCQcZ9BcxTCwSCvEAowd06_J4LUhvgKyyb0wzBAiPYm6DOHAuiiYkZxrvFF5ZpwV55hirK8Qqbe4uaOrEfNQ"

headers = {
    'authorization': f"Bearer {token}",
    'uuid': str(uuid.uuid4()),
    'accept': "application/json",
    'client_id': "7a733759-c182-443d-93f8-6e607d96b9c1",
    'content-type': 'application/json'
}

print(headers)

class Account(Resource):
	def get(self):
		conn.request("GET", "/gcb/api/v2/accounts/details", headers=headers)
		res = conn.getresponse()
		data = res.read().decode()
		dataResponse = json.loads(data)
	#	productNames = []
	#	for ccdetails in dataResponse["accountGroupDetails"][0]["creditCardAccountsDetails"]:
	#		productNames.append(ccdetails["productName"])
	#	return productNames
	#	return productNames["accountGroupDetails"]
		#dataResponse["accountGroupDetails"][0]["creditCardAccountsDetails"][0]["productName"]
		return dataResponse
		
api.add_resource(Account, "/balance")
#api.add_resource(User, "/user/{string:name: name"})
#api.add_resource(Login, "/register")

app.run(debug=True)

# get --request data, post -- login, del, put 






print("hello")

