from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class Hosttest(LiveServerTestCase):

    def test_homepage(self):
        options = Options()
        options.headless = True
        driver = webdriver.Chrome(chrome_options=options)
        driver.get("http://127.0.0.1:8000/")
        time.sleep(10)
        assert "Hello, world!" in driver.title


# class LoginFormTest(LiveServerTestCase):

#     def test_form(self):
#         driver = webdriver.Chrome()
#         driver.get("http://127.0.0.1:8000/accounts/login/")
#         time.sleep(3)
#         user_name = driver.find_element(By.NAME,'username')
#         password = driver.find_element(By.NAME,'password')
#         time.sleep(3)
#         submit = driver.find_element(By.ID,'submit')
#         user_name.send_keys('admin')
#         password.send_keys('admin')
#         submit.send_keys(Keys.RETURN)

#         assert 'admin' in driver.page_source
#         time.sleep(3)
