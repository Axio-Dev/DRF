import requests 

endpoint = "http://localhost:8000/api/products/"


data = {
    "title": "Oasis What's The Morning Story Vinil",
    "price": 51.99
}
get_response = requests.post(endpoint, json=data) # => This an API (Application Programming Interface) => Http requests

print(get_response.json())