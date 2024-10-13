import pytest
import requests
import allure

#We are automating PUT request - Update booking API

#create token using AUTH API

def Create_AUTH_token():
    #required data
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type" : "application/json"}
    payload = {
    "username" : "admin",
    "password" : "password123"
    }
    responseData = requests.post(url=URL,headers=headers,json=payload)
    print(responseData.json())
    token = responseData.json()["token"]
    print(token)
    return token

#create booking
#
def Create_booking():
    URL = "https://restful-booker.herokuapp.com/booking"
    header = headers = {"Content-Type" : "application/json"}
    payload = {
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
    responseData = requests.post(url=URL,headers=header,json=payload)
    bookingid = responseData.json()["bookingid"]
    print(bookingid)
    return bookingid

#TC - Put request
def test_Put_Update_booking():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    bookingid = str(Create_booking())
    URL = base_url + bookingid
    cookie = "token=" + Create_AUTH_token()
    header = {"Content-Type" : "application/json",
              # "Accept" : "application/json",
              "Cookie" : cookie,
              }
    payload = {
    "firstname" : "Rohit",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    response = requests.put(url=URL,headers=header,json=payload)
    print(response.json())
    assert response.status_code == 200

def test_Delete_booking():
    base_url = "https://restful-booker.herokuapp.com/booking/"
    bookingid = str(Create_booking())
    URL = base_url + bookingid
    cookie = "token=" + Create_AUTH_token()
    header = {"Content-Type" : "application/json",
              # "Accept" : "application/json",
              "Cookie" : cookie,
              }
    response = requests.delete(url=URL, headers=header)
    assert response.status_code == 201