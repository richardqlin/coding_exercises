import requests,ast

parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

#print (response.content.decode('utf-8'),type(response.content.decode('utf-8')))

ct=ast.literal_eval(response.content.decode('utf-8'))

for x in ct:
    print(x)

print(ct['response'])
