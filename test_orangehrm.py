import time


from selenium import webdriver

# from selenium.webdriver.common.by import By

from pageObjects.Add_Emp_page import AddEmplyee
from pageObjects.LoginPage import loginpage
from utilities.readproperties import readconfig
from utilities.logger import LogJenerator

# Edge_Options=webdriver.EdgeOptions()
# Edge_Options.add_argument("headless")



class Test_login:

    url=readconfig.geturl()
    username=readconfig.getusername()
    password=readconfig.getpassword()
    log=LogJenerator.loggen()
    #
    def test_page_title_001(self,setup):
        self.driver=setup
        self.log.info("test case started")
        self.driver.get(self.url)
        self.log.info("go to this url-->"+ self.url)
        # driver=webdriver.Edge(options=Edge_Options)
        # driver.get("https://opensource-demo.orangehrmlive.com/")
        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info('test case is passed')
            self.log.info("page title is -->"+self.driver.title)
        else:
            assert False

    # def test_login_002(self):
    #     driver=webdriver.Edge()
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #     driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys('Admin')
    #     driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('admin123')
    #     driver.find_element(By.XPATH,"//button[@type='submit']").click()
    #     driver.implicitly_wait(5)
    #
    #     try:
    #         time.sleep(2)
    #         driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    #         print("test_login_001 is Passed")
    #         driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
    #         driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    #         assert True
    #     except NoSuchElementException:
    #         print('test case failed')
    #         assert False
    #     def test_addemp(self):
    #         driver = webdriver.Edge()
    #         driver.implicitly_wait(10)
    #         driver.get("https://opensource-demo.orangehrmlive.com/")
    #         driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    #         driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #         driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    #         driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']").click()
    #         time.sleep(3)
    #         driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
    #         driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys('a')
    #         driver.find_element(By.XPATH,"//input[@placeholder='Middle Name']").send_keys('m')
    #         driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys('janjal')
    #         driver.find_element(By.XPATH,"//button[@type='submit']").click()
    #         time.sleep(2)
    #         try:
    #             driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']").click()
    #             driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
    #             driver.find_element(By.XPATH, "//div[@class='oxd-autocomplete-text-input oxd-autocomplete-text-input--focus']//input[@placeholder='Type for hints...']").send_keys("ajay")
    #             driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #             driver.find_element(By.XPATH,"//span[@class='oxd-text oxd-text--span']").is_displayed()
    #             assert True
    #         except:
    #             assert False

    # def test_addEmp_002(self, setup):
    #     self.driver = setup
    #     # driver = webdriver.Edge()
    #     # driver.implicitly_wait(10)
    #     # driver.get("https://opensource-demo.orangehrmlive.com/")
    #     self.lp = loginpage(self.driver)
    #
    #     self.lp.enter_Username("Admin")
    #     self.lp.enter_password("admin123")
    #     self.lp.click_login()


        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # self.driver.find_element(By.XPATH,
        #                     "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']").click()
        # self.driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
        # self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Credence")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Credence")
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Credence")
        # time.sleep(1)
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        # print(self.driver.find_element(By.XPATH,
        #                           "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']").text)
        # try:
        #     self.driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
        #     print("test_addEmp_002 is Passed")
        #     self.driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
        #     self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        #
        #     addemp=True
        # except:
        #     print("test_addEmp_002 is Failed")
        #     print("test_addEmp_002 is completed")
        #
        #     addemp=False
        #
        # if addemp==True:
        #     addemp=True
        # else:
        #     addemp=False
        # time.sleep(5)
        # print(self.lp.login_status())
        # if self.lp.login_status()==True:
            # self.lp.Click_MenuButton()
            # self.lp.Click_Logout()
        #     assert True
        # else:
        #     assert False


    def test_ad_demployee_003(self,setup):
        self.driver=setup
        self.log.info("test case started")

        self.driver.get(self.url)
        self.log.info("go to this url :"+self.url)
        self.lp = loginpage(self.driver)
        self.lp.enter_Username(self.username)
        self.log.info("entering username :"+self.username)
        self.lp.enter_password(self.password)
        self.log.info("entering password :"+self.password)
        self.lp.click_login()
        self.log.info("clicking login button")
        self.ae=AddEmplyee(self.driver)
        self.ae.click_pim()
        self.ae.Click_Add_button()
        self.log.info("adding employee button")
        time.sleep(2)
        self.ae.Enter_firstname("ajay")
        self.log.info("entering firstname:"+'ajay')
        self.ae.Enter_middlename("M")
        self.log.info("entering middlename:"+"M")

        self.ae.Enter_lastname("Testing")
        self.log.info("entering lastname:"+"Testing")

        time.sleep(2)
        self.ae.Click_save()
        self.log.info("clicking on submit button")
        time.sleep(3)
        if self.ae.Add_emoployee_status()==True:
            self.lp.Click_MenuButton()
            self.log.info("click on menu button")
            # self.driver.save_screenshot("D:\\Pytest\\ScreenShots\\loginandAddemployee.png")
            self.lp.Click_Logout()
            self.log.info("click on logout button")
            assert True
        else:
            assert False
