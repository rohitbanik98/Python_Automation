import pytest
import allure
import requests


@allure.title("testing")


def test_verify_sum():
    assert 1 + 1 == 2

@pytest.mark.smoke
def test_verify_sub():
    assert 2 - 1 == 2

@pytest.mark.skip(reason ="learning")
def test_verify_sub():
    assert 2 - 2 == 0


