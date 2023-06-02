import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Define web driver instance
@pytest.fixture(params=["Chrome", "Firefox"])
def setup(request):
    if request.param == "Chrome":
        service_obj = Service("C:\\Users\\lou_m\\OneDrive\\Documentos\\ChromeDriver")
        driver = webdriver.Chrome(service=service_obj)
    else:
        service_obj = Service("C:\\Users\\lou_m\\OneDrive\\Documentos\\GeckoDriver")
        driver = webdriver.Firefox(service=service_obj)

    # Go to our testing page
    driver.get("https://ultimateqa.com/automation")
    driver.maximize_window()
    # Returning driver instance
    return driver


@pytest.fixture()
def setup_response():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.request("GET", url)
    response_info = {"responseCode": response.status_code, "responseBody": response.json()}
    return response_info

