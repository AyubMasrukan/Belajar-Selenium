import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as expected_conditions


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))

    def test_Login_Negative_NoPassword(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # membuka web
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("standard_user")  # username salah
        time.sleep(1)
        driver.find_element(By.ID, "password").send_keys(
            "")  # password benar
        time.sleep(1)
        driver.find_element(By.ID, "login-button").click()

        response_message = driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]").text
        self.assertEqual(response_message,
                         'Epic sadface: Password is required')

    def test_Login_valid(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # membuka web
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("standard_user")  # username valid
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # password valid
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()

    def test_Logout(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # membuka web
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("standard_user")  # username valid
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # password valid
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "logout_sidebar_link").click()

    def test_About(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # membuka web
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("standard_user")  # username valid
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # password valid
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "about_sidebar_link").click()
        time.sleep(5)

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # membuka web
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("standard_user")  # username valid
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # password valid
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(2)

    def test_your_cart(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")  # membuka web
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(
            By.ID, "user-name").send_keys("standard_user")  # username valid
        time.sleep(2)
        driver.find_element(By.ID, "password").send_keys(
            "secret_sauce")  # password valid
        time.sleep(2)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)


unittest.main()
