import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver


class loginpage:
    text_username_xpath=(By.XPATH, "//input[@placeholder='Username']")
    text_password_xpath=(By.XPATH, "//input[@placeholder='Password']")
    click_login_button_xpath=(By.XPATH, "//button[normalize-space()='Login']")
    click_menu_button_xpath=(By.XPATH, "//p[@class='oxd-userdropdown-name']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver=driver

    def enter_Username(self,Username):
        self.driver.find_element(*loginpage.text_username_xpath).send_keys(Username)

    def enter_password(self,password):
        self.driver.find_element(*loginpage.text_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(*loginpage.click_login_button_xpath).click()

    def Click_MenuButton(self):
        self.driver.find_element(*loginpage.click_menu_button_xpath).click()

    def Click_Logout(self):
        self.driver.find_element(*loginpage.Click_Logout_XPATH).click()

    def login_status(self):

        try:
            self.driver.find_element(*loginpage.click_menu_button_xpath)
            return True
        except NoSuchElementException:
            return False