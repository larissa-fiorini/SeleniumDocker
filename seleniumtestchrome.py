from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

SELENIUM_SERVER_URL = "http://localhost:4444/wd/hub"

options = Options()
driver=webdriver.Remote(
    command_executor=SELENIUM_SERVER_URL,
    options=options
)

driver.get("https://example.com")

print(driver.title)

driver.quit()