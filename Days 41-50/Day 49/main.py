from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options)
driver.get("https://tinyurl.com/5884jyf")

login_button = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
login_button.click()
email = driver.find_element(By.NAME, "session_key")
email.send_keys("")
password = driver.find_element(By.NAME, "session_password")
password.send_keys("")
enter_account = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
enter_account.click()
time.sleep(3)
all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-list__title")

for listing in all_listings:
    listing.click()
    time.sleep(2)

    try:
        job_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        job_button.click()
        time.sleep(2)
        send_curriculum_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
        send_curriculum_button.click()
        time.sleep(2)
        select_curriculum = driver.find_element(By.CSS_SELECTOR, ".jobs-resume-picker__resume-btn-container #ember1976")
        select_curriculum.click()
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer span")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue
