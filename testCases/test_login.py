import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("************* Test_001_Login **********")
        self.logger.info("************* Verifying Home Page Title **********")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "nopCommerce demo store. Login":
            assert True
            self.driver.close()
            self.logger.info("************* Home Page Title test is passed **********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************* Home Page Title test is failed **********")
            assert False

    # def test_login(self,setup):
    #     self.logger.info("************* Verifying Login test **********")
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.lp = LoginPage(self.driver)
    #     self.lp.setUsername(self.username)
    #     self.lp.setPassword(self.password)
    #     self.lp.clickLogin()
    #     act_title = self.driver.title
    #     self.logger.info(f"Actual title after login: {act_title}")
    #     if act_title == "Dashboard / nopCommerce administration":
    #         self.logger.info("************* Login test is passed **********")
    #         self.driver.close()
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
    #         self.driver.close()
    #         self.logger.error("************* Login test is failed **********")
    #         assert False
    def test_login(self, setup):
        self.logger.info("************* Verifying Login test **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        try:
            # Wait for a reliable element instead of the title
            dashboard_element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Dashboard')]"))
            )
            self.logger.info("************* Login test is passed **********")
            assert dashboard_element is not None
        except Exception as e:
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            actual_title = self.driver.title
            self.logger.error(f"************* Login test failed. Actual title: {actual_title} **********")
            assert False
        finally:
            self.driver.close()