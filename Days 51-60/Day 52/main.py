from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


class InstaFollower:
    """
    Finds followers of a popular Instagram account and follows them
    """

    INSTA_ACCOUNT_TO_FOLLOW = 'INSTA ACCOUNT YOU ARE INTERESTED IN'
    INSTA_USERNAME = 'YOUR USER NAME'
    INSTA_PSW = 'YOUR INSTA PASSWORD'

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        user_field = self.driver.find_element(By.CSS_SELECTOR, '#loginForm input')
        user_field.send_keys(self.INSTA_USERNAME)
        psw_field = self.driver.find_element(By.NAME, 'password')
        psw_field.send_keys(self.INSTA_PSW)
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        login_btn.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{self.INSTA_ACCOUNT_TO_FOLLOW}")
        time.sleep(7)
        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        time.sleep(6)
        followers.click()
        time.sleep(3)

    def follow(self):
        while True:
            try:

                list_of_people = self.driver.find_elements(By.CSS_SELECTOR, 'button')
                print(len(list_of_people))
                for person in list_of_people:
                    print(person.text)
                    if person.text == "Follow":
                        time.sleep(random.randint(1000, 1600) / 1000)
                        self.driver.execute_script("arguments[0].click();", person)
                        time.sleep(random.randint(30, 60))
                    print(len(list_of_people))
                print('Scrolling...')

                fBody = self.driver.find_element(By.XPATH, "//div[@class='_aano']")
                scroll = 0
                while scroll < 5:  # scroll 5 times, feel free to change this
                    self.driver.execute_script(
                        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
                    time.sleep(2)
                    scroll += 1
            except Exception as e:
                print(e)


if __name__ == '__main__':
    insta = InstaFollower()
    insta.login()
    insta.find_followers()
    insta.follow()
