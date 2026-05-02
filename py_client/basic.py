import requests 

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Mictlan PC","content": "PC Master Race", "price": "abc123"}) # => This an API (Application Programming Interface) => Http requests

print(get_response.json())


