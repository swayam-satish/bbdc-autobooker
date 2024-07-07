import time
from captcha_solver import CaptchaSolver

import captcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twocaptcha import TwoCaptcha
import sys
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL")
LOGIN_ID = os.getenv("LOGIN_ID")
PASSWORD = os.getenv("PASSWORD")
API_KEY = os.getenv("API_KEY")


class DrivingClass:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)

    def loging_in(self):
        self.driver.get(URL)
        time.sleep(2)
        id_button = self.driver.find_element(By.ID, value="input-8")
        id_button.click()
        id_button.send_keys(LOGIN_ID)

        password_button = self.driver.find_element(By.ID, value="input-15")
        password_button.click()
        password_button.send_keys(PASSWORD)

        login_button = self.driver.find_element(By.XPATH, value='//*[@id="app"]/div/div/div[1]/div/div/form/div/div['
                                                                '5]/button/span')
        login_button.click()

    def captcha_solver(self):
        time.sleep(6)
        captcha_img = self.driver.find_element(By.CLASS_NAME, value="v-responsive__content")
        captcha_img.screenshot("captchas/captcha.png")

        # https://github.com/2captcha/2captcha-python
        time.sleep(2)

        api_key = os.getenv('APIKEY_2CAPTCHA', API_KEY)

        solver = TwoCaptcha(api_key)

        try:
            result = solver.normal('captchas/captcha.png')["code"]
            return result

        except Exception as e:
            print(e)

        else:
            print(result)

    def final_captcha(self, result):
        solver = CaptchaSolver(result)
        solver.all_caps()
        solver.one_letter()
        solver.consecutive_letters()
        solver.alternate_letters()
        solver.two_in_between()
        solver.triplets()
        final_captcha_list = solver.final_list()
        return final_captcha_list

    def fillout_captcha(self, mylist):
        for captcha in mylist:
            try:
                time.sleep(8)
                captcha_input = self.driver.find_element(By.XPATH, value='//*[@id="input-30"]')
                captcha_input.send_keys(Keys.CONTROL, "a")
                captcha_input.send_keys(Keys.DELETE)
                captcha_input.click()
                captcha_input.send_keys(captcha)
                time.sleep(2)
                captcha_submit_button = self.driver.find_element(By.CLASS_NAME, value="v-btn__content")
                captcha_submit_button.click()
            except NoSuchElementException or ElementNotInteractableException:
                break


bot = DrivingClass()
bot.loging_in()
result = bot.captcha_solver()
print(result)
captcha_list = bot.final_captcha(result)
bot.fillout_captcha(captcha_list)
