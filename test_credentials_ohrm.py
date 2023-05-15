

from pageObjects.LoginPage import loginpage
from utilities.logger import LogJenerator
from utilities.readproperties import readconfig


class Test_Credential_001:
    url = readconfig.geturl()
    log = LogJenerator.loggen()


    def test_001(self,setup,getDataforlogin):
            self.driver = setup
            self.log.info("test case started")
            self.driver.get(self.url)
            self.log.info("go to this url :" + self.url)
            self.lp = loginpage(self.driver)
            self.lp.enter_Username(getDataforlogin[0])
            self.log.info("entering username :" + getDataforlogin[0])
            self.lp.enter_password(getDataforlogin[1])
            self.log.info("entering password :" + getDataforlogin[1])
            self.lp.click_login()
            self.log.info("clicking login button")
            if self.lp.login_status()==True:
                if getDataforlogin[2] == 'pass':
                    self.lp.Click_MenuButton()
                    self.log.info("Click on Menu button")
                    self.lp.Click_Logout()
                    self.log.info("Click on logout button")
                    self.log.info("test_case is Passed")
                    assert True
                else:
                    assert False

            else:
                if getDataforlogin[2] == 'fail':
                    self.log.info("test_caase is Passed")
                    assert True
                else:
                     assert False
