from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
timeout_5_minutes = time() + 300
while time() < timeout_5_minutes:
    timeout_5_seconds = time() + 5

    while time() < timeout_5_seconds:
        cookie.click()
    store_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    for item in range(len(store_items)-1, 0, -1):
        try:
            store_items[item].get_attribute('onclick')
            store_items[item].click()
        except:
            pass

cookies_per_second = driver.find_element(By.ID, "cps")
print(cookies_per_second.text)

driver.quit()
