import requests

r = requests.get('http://localhost:5000/getMessages').json()
for entry in r:
    print (entry['_id']['$oid'])