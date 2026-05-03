import requests 

endpoint = "http://localhost:8000/api/products/4398528023457843208"

get_response = requests.get(endpoint) # => This an API (Application Programming Interface) => Http requests

print(get_response.json())
