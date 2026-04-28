import requests 

endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query": "Hello world!"}) # => This an API (Application Programming Interface) => Http requests

# print(get_response.text) # Printing raw text response
# print(get_response.status_code)
print(get_response.json()['message'])

# A Http request gives you a HTML response 
# A REST API HTTP requests gives you a JSON response

