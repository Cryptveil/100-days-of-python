from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
driver.get("https://www.twitter.com")
time.sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div/div/div/div[1]/a')
login_button.click()
time.sleep(4)
username = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
username.send_keys("grellheist")
next_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
next_button.click()
time.sleep(4)
password = driver.find_element(By.NAME, "password")
password.send_keys("HJGameplays@1")
enter = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
enter.click()
time.sleep(6)
tweet_something = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
tweet_something.click()
time.sleep(3)
write = driver.find_element(By.CSS_SELECTOR, '[aria-label = "Texto do Tweet"]')
write.send_keys("Esse Tweet foi feito por um bot feito em Python e se vc está vendo isso vc é foda (mas vou excluir o tweet)")
send_tweet = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
send_tweet.click()
