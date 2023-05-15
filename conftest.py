import pytest
from selenium import webdriver



# from test_orangehrm import Edge_Options

#
@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    # driver.get("https://opensource-demo.orangehrmlive.com/")
    return driver

# In pytest, hook functions are functions that can be used to extend or
# modify the behavior of pytest. They are called automatically by pytest at
# specific times during the test run.

# The pytest_configure function is a hook function in pytest that is called once the
# configuration object has been created and all plugins and initial conftest files have been loaded.

# The pytest_addoption function is a hook function in pytest that is used to add custom command-line options to the
# pytest command. It takes a single argument, parser, which is an instance of the argparse.ArgumentParser class.

def pytest_addoption(parser):
    parser.addoption("--browser")


# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method
# to get the value of the --browser option passed to pytest on the command line.

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver=webdriver.Chrome()
#         print("launching chrome")
#     elif browser == 'edge':
#         driver = webdriver.Edge()
#         print("launching edge")
#     else:
#         print("Headless")
#         edge_options = webdriver.EdgeOptions()
#         edge_options.add_argument('headless')
#         driver = webdriver.Edge(options=edge_options)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     return driver

# @ytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("Launching Chrome Browser")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching Firefox Browser")
#     elif browser == 'edge':
#         print("Launching Edge Browser")
#         driver = webdriver.Edge()
#     else:
#         print("Headless mode")
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#         driver = webdriver.Chrome(options=chrome_options)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     return driver


# The pytest_metadata function is a hook function in pytest that allows you to
# add custom metadata to the test report. This metadata can be used to provide
# additional information about the test run, such as the environment, the test data,
# or any other relevant information.

def pytest_metadata(metadata):
        # To Add
        metadata["Environment"]='Test'
        metadata["Project Name"]='OrangeHRM'
        metadata["Mopdule Name"]="Login"
        metadata["Tester"]="Ajay"
        # To remove
        metadata.pop("Packages",None)
        metadata.pop("Plugins",None)

# @pytest.fixture(params=[
#     ("Admin","admin123","pass"),
#     ("Admin1","admin123","fail"),
#     ("Admin","admin1231","fail"),
#     ("Admin1","admin1231","fail")
#
# ])
#
# def getDataforlogin(request):
#     return request.param



