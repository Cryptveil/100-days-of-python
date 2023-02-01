from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": event_names[n].text
    }

print(events)
driver.quit()
