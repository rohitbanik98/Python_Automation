import pytest
import allure
import requests


@allure.title("Positive")

#positive TC
def test_get_single_request_by_id1():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.status_code)
    assert response_data.status_code == 200

@allure.title("Negative")
#negative TC
def test_get_single_request_by_id2():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404