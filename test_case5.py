import time

from selenium import webdriver
from selenium.webdriver.common.by import By

Edge_options=webdriver.EdgeOptions()
Edge_options.add_argument("headless")

class Test_browser:
    def test_browser1(self):
        driver=webdriver.Edge(options=Edge_options)
        driver.get("https://credence.in/")
        offers=driver.find_element(By.XPATH,"//span[@class='text-white b label']").text
        print(offers)
        print(driver.title)
        if driver.title=="Credence":
            assert True
        else:
            assert False
    #
    # def test_browser2(self):
    #     driver=webdriver.Edge(options=Edge_options)
    #     driver.get("https://credence.in/")
    #     driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()
    #     time.sleep(4)
    #     l=len(driver.find_elements(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a"))
    #     time.sleep(4)
    #
    #     list=[]
    #     for r in range(1, l+1):
    #         contact = driver.find_element(By.XPATH, "//div[@class='quickfinder-description gem-text-output']//p//a["+str(r)+"]").text
    #         # print(contact)
    #         list.append(contact)
    #     if "+91 9091929355" in list:
    #         assert True
    #     else:
    #         assert False