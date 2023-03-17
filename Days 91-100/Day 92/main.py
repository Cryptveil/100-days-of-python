from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json

options = Options()
options.add_experimental_option("detach", False)
driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
driver.get("https://steamdb.info/app/39210/charts/")

player_count = driver.find_element(By.XPATH,
                                   "/html/body/div[4]/div[1]/div[2]/div/div[2]/div[4]/ul/li[2]/strong")
player_day_peak = driver.find_element(By.XPATH,
                                      "/html/body/div[4]/div[1]/div[2]/div/div[2]/div[4]/ul/li[3]/strong")

data = {
    "player_count": player_count.text,
    "player_day_peak": player_day_peak.text
}

with open("data.json", "w") as file:
    json.dump(data, file)
