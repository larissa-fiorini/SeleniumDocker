from selenium import webdriver
from selenium.webdriver.firefox.options import Options

SELENIUM_SERVER_URL = "http://localhost:4442/wd/hub"

options = Options()
options.headless = False

driver = webdriver.Remote(
    command_executor=SELENIUM_SERVER_URL,
    options=options
)


driver.get("https://example.com")

print(driver.title)

driver.quit()
