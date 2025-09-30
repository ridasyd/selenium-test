from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = Options()
# enter path of chromium on your computer
chrome_options.binary_location = r"C:\Chromium\Application\chrome.exe"
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# enter path of chromedriver
service = Service(r"C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# enter the website you want to scrape
driver.get("https://www.studocu.com/de")
print(driver.title)

try:
    wait = WebDriverWait(driver, 15)

    # wait until the search input exists & is visible
    search = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input[type='search']"))
    )

    search.clear()
    search.send_keys("test")  # enter what you want to search for
    search.send_keys(Keys.RETURN)

    print("Search submitted!")

    # wait for results to load, look for a document card
    cards = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "div.DocumentCardRich_header__8ueqN")
        )
    )

    for card in cards:
        print(card.text)
        print()

finally:
    driver.quit()
