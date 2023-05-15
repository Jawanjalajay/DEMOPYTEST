from pageObjects.Add_Emp_page import AddEmplyee
from pageObjects.LoginPage import loginpage
from utilities import XLutils
from utilities.readproperties import readconfig
from utilities.logger import LogJenerator
import time


class Test_excel_data:
    url = readconfig.geturl()
    username = readconfig.getusername()
    password = readconfig.getpassword()
    log = LogJenerator.loggen()
    path = "D:\\Pytest\\TestData\\EmployeeList.xlsx"

    # def test_ad_demployee_005(self, setup):
    #     self.driver = setup
    #     self.log.info("test case started")
    #
    #     self.driver.get(self.url)
    #     self.log.info("go to this url : " + self.url)
    #     self.lp = loginpage(self.driver)
    #     self.lp.enter_Username(self.username)
    #     self.log.info("entering username : " + self.username)
    #     self.lp.enter_password(self.password)
    #     self.log.info("entering password : " + self.password)
    #     self.lp.click_login()
    #     self.log.info("clicking login button")
    #     time.sleep(1)
    #     self.ae = AddEmplyee(self.driver)
    #     self.rows = XLutils.getrowCount(self.path, "Sheet1")
    #     self.ae.click_pim()
    #     self.ae.Click_Add_button()
    #     self.log.info("adding employee button")
    #
    #     # print("no of rows are :", self.rows)
    #     # self.Firstname=XLutils.readData(self.path,'Sheet1',3,2)
    #     # print(self.Firstname)
    #     #
    #     # for r in range(1,self.rows+1):
    #     #     self.Firstname=XLutils.readData(self.path,'Sheet1',5,r)
    #     #     print(self.Firstname)
    #     # time.sleep(2)
    #     status_list = []
    #     for r in range(2, self.rows + 1):
    #         self.firstName = XLutils.readData(self.path, 'Sheet1', r, 2)
    #         self.middleName = XLutils.readData(self.path, 'Sheet1', r, 3)
    #         self.lastName = XLutils.readData(self.path, 'Sheet1', r, 4)
    #         # print(self.firstname,self.middlename,self.lastname)
    #         # time.sleep(1)
    #         self.ae.Enter_firstname(self.firstName)
    #         self.log.info("entering firstname: " + self.firstName)
    #         self.ae.Enter_middlename(self.middleName)
    #         self.log.info("entering middlename: " + self.middleName)
    #         self.ae.Enter_lastname(self.lastName)
    #         self.log.info("entering lastname: " + self.lastName)
    #         time.sleep(2)
    #         self.ae.Click_save()
    #         self.log.info("clicking on submit button")
    #         time.sleep(2)
    #
    #         if self.ae.Add_emoployee_status() == True:
    #             self.ae.Click_AddEmployee()
    #             status_list.append("pass")
    #             self.driver.save_screenshot("D:\\Pytest\\ScreenShots\\loginandAddemployee1.png")
    #             self.log.info("test case is passed")
    #             assert True
    #         else:
    #             status_list.append("pass")
    #             self.log.info("test case is failed")
    #             assert False
    #     print(status_list)
    #     self.lp.Click_MenuButton()
    #     self.log.info("click on menu button")
    #
    #     self.lp.Click_Logout()
    #     self.log.info("click on logout button")

    def test_ad_demployee_006(self, setup):
        self.driver = setup
        self.log.info("test case started")

        self.driver.get(self.url)
        self.log.info("go to this url : " + self.url)
        self.lp = loginpage(self.driver)
        self.lp.enter_Username(self.username)
        self.log.info("entering username : " + self.username)
        self.lp.enter_password(self.password)
        self.log.info("entering password : " + self.password)
        self.lp.click_login()
        self.log.info("clicking login button")
        time.sleep(1)
        self.ae = AddEmplyee(self.driver)
        self.rows = XLutils.getrowCount(self.path, "Sheet1")
        self.ae.click_pim()
        self.ae.Click_Add_button()
        self.log.info("adding employee button")

        # print("no of rows are :", self.rows)
        # self.Firstname=XLutils.readData(self.path,'Sheet1',3,2)
        # print(self.Firstname)
        #
        # for r in range(1,self.rows+1):
        #     self.Firstname=XLutils.readData(self.path,'Sheet1',5,r)
        #     print(self.Firstname)
        # time.sleep(2)
        status_list = []
        for r in range(2, self.rows + 1):
            self.firstName = XLutils.readData(self.path, 'Sheet1', r, 2)
            self.middleName = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.lastName = XLutils.readData(self.path, 'Sheet1', r, 4)
            # print(self.firstname,self.middlename,self.lastname)
            # time.sleep(1)
            self.ae.Enter_firstname(self.firstName)
            self.log.info("entering firstname: " + self.firstName)
            self.ae.Enter_middlename(self.middleName)
            self.log.info("entering middlename: " + self.middleName)
            self.ae.Enter_lastname(self.lastName)
            self.log.info("entering lastname: " + self.lastName)
            time.sleep(2)
            self.ae.Click_save()
            self.log.info("clicking on submit button")
            time.sleep(2)

            if self.ae.Add_emoployee_status() == True:
                self.ae.Click_AddEmployee()
                status_list.append("pass")
                XLutils.writeData(self.path,"Sheet1",r,5,"pass")
                self.driver.save_screenshot("D:\\Pytest\\ScreenShots\\loginandAddemployee1.png")

            else:
                status_list.append("fail")
                XLutils.writeData(self.path, "Sheet1", r, 5, "fail")
                self.driver.save_screenshot("D:\\Pytest\\ScreenShots\\loginandAddemployee1.png")

        print(status_list)
        self.lp.Click_MenuButton()
        self.log.info("click on menu button")
        self.lp.Click_Logout()
        self.log.info("click on logout button")
        self.driver.close()
        if "fail" not in status_list:
            self.log.info("test case is passed")
            assert True
        else:
            self.log.info("test case is failed")
            assert False
        self.log.info("test case is completed")