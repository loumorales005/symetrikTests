from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# This is added just to avoid warning and error messages
serviceObj = Service("C:\\Users\\lou_m\\OneDrive\\Documentos\\ChromeDriver")
driver = webdriver.Chrome(service=serviceObj)

# Locator to get <h2> element text -> We pick second h2 child under the <main> tag
h2Text = driver.find_element(By.CSS_SELECTOR, "main h2:nth-child(2)").text

# Locator to get <p> element text -> We pick second p child under the <main> tag
pText = driver.find_element(By.CSS_SELECTOR, "main p:nth-child(2)").text

# It could also work just selecting the second h2 or p child from the whole DOM
h2Text_2 = driver.find_element(By.CSS_SELECTOR, "h2:nth-child(2)").text
pText_2 = driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)").text
