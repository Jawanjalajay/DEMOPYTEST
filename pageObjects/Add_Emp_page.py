import time

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException as ec

class AddEmplyee:
         Click_pim_xpath=(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
         Click_add_button_xpath=(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")
         Text_firstname_xpath=(By.XPATH, "//input[@placeholder='First Name']")
         Text_middlename_xpath=(By.XPATH, "//input[@placeholder='Middle Name']")
         Text_lastname_xpath=(By.XPATH, "//input[@placeholder='Last Name']")
         Click_save_button=(By.XPATH, "//button[@type='submit']")
         PersonalDetails_Tab_XPATH = (By.XPATH, "//h6[normalize-space()='Personal Details']")
         Click_Add_Emp_XPATH = (By.XPATH, "//a[normalize-space()='Add Employee']")

         def __init__(self,driver):
                 self.driver=driver

         def click_pim(self):
                self.driver.find_element(*AddEmplyee.Click_pim_xpath).click()

         def Click_Add_button(self):
                 self.driver.find_element(*AddEmplyee.Click_add_button_xpath).click()

         def Enter_firstname(self,firstname):
              self.driver.find_element(*AddEmplyee.Text_firstname_xpath).send_keys(firstname)

         def Enter_middlename(self,middlename):
               self.driver.find_element(*AddEmplyee.Text_middlename_xpath).send_keys(middlename)

         def Enter_lastname(self,lastname):
                 self.driver.find_element(*AddEmplyee.Text_lastname_xpath).send_keys(lastname)

         def Click_save(self):
                 self.driver.find_element(*AddEmplyee.Click_save_button).click()

         def Click_AddEmployee(self):
             self.driver.find_element(*AddEmplyee.Click_Add_Emp_XPATH).click()

         def Add_emoployee_status(self):
          time.sleep(5)
          try:
             self.driver.find_element(*AddEmplyee.PersonalDetails_Tab_XPATH)
             return True
          except ec:
             return False