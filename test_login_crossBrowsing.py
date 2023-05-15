import time

from pageObjects.Add_Emp_page import AddEmplyee
from pageObjects.LoginPage import loginpage
from utilities.readproperties import readconfig
from utilities.logger import LogJenerator


class Test_crossBrowse:

    url=readconfig.geturl()
    username=readconfig.getusername()
    password=readconfig.getpassword()

    log=LogJenerator.loggen()

    def test_ohrm_login_001(self, setup):
        self.driver = setup
        self.log.info("test case started")

        self.driver.get(self.url)
        self.log.info("go to this url :" + self.url)
        time.sleep(5)
        self.lp = loginpage(self.driver)
        self.lp.enter_Username(self.username)
        self.log.info("entering username :" + self.username)
        self.lp.enter_password(self.password)
        self.log.info("entering password :" + self.password)
        self.lp.click_login()
        self.log.info("clicking login button")
        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info('test case is passed')
            self.log.info("page title is -->" + self.driver.title)
        else:
            assert False
        self.driver.close()