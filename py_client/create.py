import requests 

endpoint = "http://localhost:8000/api/products/"

headers = {
    'Authorization': 'Bearer 44bbf8ea855a4f0b506cea0806f9049596c54559'
}


data = {
    "title": "Oasis What's The Morning Story Vinil",
    "price": 51.99
}
get_response = requests.post(endpoint, json=data, headers=headers) # => This an API (Application Programming Interface) => Http requests

print(get_response.json())