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
driver.get("")
