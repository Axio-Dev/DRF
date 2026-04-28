import requests 

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello world!"}) # => This an API (Application Programming Interface) => Http requests

print(get_response.text) # Printing raw text response


# A Http request gives you a HTML response 
# A REST API HTTP requests gives you a JSON response

print(get_response.json())
print(get_response.status_code)
