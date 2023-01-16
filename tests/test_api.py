import requests

ENDPOINT = "http://127.0.0.1:5000/"

def test_api_home():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_username_valid():
    response = requests.get(ENDPOINT + 'api/ashank2603')
    assert response.status_code == 200

def test_username_invalid():
    response = requests.get(ENDPOINT + 'api/ashank263')
    assert response.status_code == 404