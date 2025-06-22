import pytest
from selenium import webdriver
# import undetected_chromedriver as uc

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")  # Default to Chrome

@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser.........")
    # else:
    #     driver = webdriver.Ie()

    driver.maximize_window()
    return driver

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############## PyTest HTML Report ##################

# It is hook for adding environment info to html report
def pytest_configure(config):
    #config._metadata['Project Name'] = 'nop Commerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'Sanjana'
    config.stash.setdefault("html", {})
    metadata = config.stash["html"].setdefault("metadata", {})
    metadata["Project Name"] = "nop Commerce"
    metadata["Module Name"] = "Login"
    metadata["Tester"] = "Sanjana"

# It is hook for delete/modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)