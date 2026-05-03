import requests 

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Toast maker",
    "price": 29.55,
    "content": None
}

get_response = requests.put(endpoint, json=data) # => This an API (Application Programming Interface) => Http requests

print(get_response.json())


