# import time
#
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
#
#
# class Test_Login:
#
#     def test_login_001(self):
#         driver = webdriver.Firefox()
#         driver.implicitly_wait(10)
#         driver.get("https://opensource-demo.orangehrmlive.com/")
#         driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
#         driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin1234")
#         driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
#         try:
#             time.sleep(2)
#             driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']")
#             print("test_login_001 is Passed")
#             driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
#             driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
#             assert True
#         except NoSuchElementException:
#             print("test_login_001 is Failed")
#             print("test_login_001 is completed")
#             assert False

    # def test_addEmp_002(self):
    #     driver = webdriver.Firefox()
    #     driver.implicitly_wait(10)
    #     driver.get("https://opensource-demo.orangehrmlive.com/")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    #     driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    #     driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']").click()
    #     driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']").click()
    #     driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Credence")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']").send_keys("Credence")
    #     driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Credence")
    #     time.sleep(1)
    #     driver.find_element(By.XPATH, "//button[@type='submit']").click()
    #     print(driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-title oxd-toast-content-text']").text)
    #     try:
    #         driver.find_element(By.XPATH, "//h6[normalize-space()='Personal Details']")
    #         print("test_addEmp_002 is Passed")
    #         driver.find_element(By.XPATH, "//span[@class='oxd-userdropdown-tab']").click()
    #         driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    #         assert True
    #     except:
    #         print("test_addEmp_002 is Failed")
    #         print("test_addEmp_002 is completed")
    #         assert False
    #
    #
