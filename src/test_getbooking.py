import pytest
import allure
import requests


@allure.title("testing")

def test_get_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    assert response_data.status_code == 200