import pytest
import requests


@pytest.mark.usefixtures("setup_response")
def test_validate_response_code(setup_response):
    url = "https://jsonplaceholder.typicode.com/todos/1"
    print(f"\nResponse Code: {setup_response['responseCode']}")
    print(f"Response Body: {setup_response['responseBody']}")
    assert setup_response['responseCode'] == 200 and setup_response['responseBody'] != "", \
        "There was an error with request"





