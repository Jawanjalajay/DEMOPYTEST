
from pageObjects.LoginPage import loginpage
from utilities import XLutils
from utilities.readproperties import readconfig
from utilities.logger import LogJenerator
import time


class Test_excel_data:
    url = readconfig.geturl()
    log = LogJenerator.loggen()
    path = "D:\\Pytest\\TestData\\LoginData.xlsx"

    def test_login_008(self , setup):
        self.driver = setup
        self.log.info("test case started")

        self.driver.get(self.url)
        self.log.info("go to this url : " + self.url)
        self.lp = loginpage(self.driver)
        self.rows=XLutils.getrowCount(self.path,"Sheet1")
        # time.sleep(2)
        status_list=[]
        for r in range(2, self.rows+1):
            self.Username=XLutils.readData(self.path, "Sheet1", r, 2)
            self.Password=XLutils.readData(self.path, "Sheet1", r, 3)
            self.lp.enter_Username(self.Username)
            self.log.info("entering username : " + self.Username)
            self.lp.enter_password(self.Password)
            self.log.info("entering password : " + self.Password)
            self.lp.click_login()
            self.log.info("clicking login button")
            # time.sleep(2)
            if self.lp.login_status() == True:

                self.lp.Click_MenuButton()
                self.log.info("Click on Menu button")
                self.lp.Click_Logout()
                self.log.info("Click on logout button")
                status_list.append("pass")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Pass")

            else:
                status_list.append("fail")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")



        print(status_list)
        if "Fail" not in status_list:
            self.log.info("test_login_008 is Passed")
            assert True
        else:
            self.log.info("test_login_008 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_008 is Completed")

    # def test_login_ddt_006(self, setup):
    #     self.driver = setup
    #     self.log.info("test_login_ddt_006 is started")
    #     self.log.info("Opening Browser")
    #     self.driver.get(self.url)
    #     self.log.info("Go to this url-->" + self.url)
    #     self.lp = loginpage(self.driver)
    #     self.rows = XLutils.getrowCount(self.path, 'Sheet1')
    #     print("Number of rows are --->", self.rows)
    #     login_stuats = []
    #     for r in range(2, self.rows + 1):
    #         self.username = XLutils.readData(self.path, 'Sheet1', r, 2)
    #         self.password = XLutils.readData(self.path, 'Sheet1', r, 3)
    #
    #         self.lp.enter_Username(self.username)
    #         self.log.info("Entering username-->" + self.username)
    #         self.lp.enter_password(self.password)
    #         self.log.info("Entering password-->" + self.password)
    #         self.lp.click_login()
    #         self.log.info("Click on login button")
    #
    #         if self.lp.login_status() == True:
    #
    #             # self.driver.save_screenshot(
    #             #     "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\" + self.username + self.password + "test_login_ddt_006-pass.png")
    #             self.lp.Click_MenuButton()
    #             self.log.info("Click on Menu button")
    #             self.lp.Click_Logout()
    #             self.log.info("Click on logout button")
    #
    #             login_stuats.append("Pass")
    #             XLutils.writeData(self.path, 'Sheet1', r, 4, "Pass")
    #         else:
    #
    #             login_stuats.append("Fail")
    #             XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
    #             # self.driver.save_screenshot(
    #             #     "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\" + self.username + self.password + "test_login_ddt_006-fail.png")
    #             # assert False
    #
    #     print(login_stuats)
    #     if "Fail" not in login_stuats:
    #         self.log.info("test_login_ddt_006 is Passed")
    #         assert True
    #     else:
    #         self.log.info("test_login_ddt_006 is Failed")
    #         assert False
    #     self.driver.close()
    #     self.log.info("test_login_ddt_006 is Completed")
    #
    #
