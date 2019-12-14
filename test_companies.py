import requests

def test_get_request(requests_mock):
    requests_mock.get("https://betalist.com/regions/australia", text="Hello!")

    response = requests.get("https://betalist.com/regions/australia")

    assert response.text == "Hello!"
