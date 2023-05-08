import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
Edge_options=webdriver.EdgeOptions()
Edge_options.add_argument("headless")


class Test_c:
    @pytest.mark.Ajay
    def test_google_logo(self):
        driver=webdriver.Edge(options=Edge_options)
        driver.get("https://www.google.com/")
        logo=driver.find_element(By.XPATH,"//img[@alt='Google']").is_displayed()
        if logo==True:
            assert True
        else:
            assert False

class Test_D:
    def test_sum(self):
        a=4
        b=7
        sum=4+7
        if sum==110:
            assert True
        else:
            assert False