from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver")
# driver.get(
#     "https://www.dyson.co.kr/products/haircare/haircare/airwrap/overview?q=%EC%97%90%EC%96%B4%EB%9E%A9"
# )
driver.get(
    "https://www.dyson.co.kr/products/haircare/haircare/airwrap/overview?q=%EC%97%90%EC%96%B4%EB%9E%A9"
)

while True:
    cards = driver.find_elements(by=By.CLASS_NAME, value="card__pricing")
    driver.get(driver.current_url)
    time.sleep(3)