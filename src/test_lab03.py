#Import the packages

import pytest
import requests
import allure

@allure.title("TC#1 - Create booking CRUD positive")
@allure.description("TC#1 - Verify the create booking")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload_body = {
        "firstname" : "Rohit",
        "lastname" : "Banik",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(url = URL,headers= headers,json=payload_body )
    print(response.json())
    assert response.json()["booking"]["firstname"] == "Rohit"

@allure.title("TC#2 - Create booking CRUD positive")
@allure.description("TC#2 - Verify the status code")
@pytest.mark.crud
def test_create_booking_positive_tc2():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload_body = {
        "firstname" : "Rohit",
        "lastname" : "Banik",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(url = URL,headers= headers,json=payload_body )
    print(response.json())
    assert response.status_code == 201

@allure.title("TC#3 - Create booking CRUD positive")
@allure.description("TC#3 - Verify the booking ID is not none")
@pytest.mark.crud
def test_create_booking_positive_tc3():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type" : "application/json"}
    payload_body = {
        "firstname" : "Rohit",
        "lastname" : "Banik",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = requests.post(url = URL,headers= headers,json=payload_body )
    print(response.json())
    assert response.json()["bookingid"] > 0