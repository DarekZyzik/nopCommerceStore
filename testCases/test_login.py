from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import logging

class Test_001_Login:

    base_url = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()


    def test_homePage_Title(self, setup):

        self.logger.error('*******************Test_001_Login******************')
        self.logger.error('*************Verifying Home Page Title ************')
        self.driver = setup
        self.driver.get(self.base_url)

        act_title = self.driver.title
        if act_title == 'Your store. Login123':
            assert True
            self.driver.close()
            self.logger.error('*************Home Page Title test is PASSED ************')
        else:
            self.driver.save_screenshot(r"C:\Users\Daro\PycharmProjects\nopCommerceStore\Screenshots\test_homePage_Title.png")
            self.driver.close()
            self.logger.error('*************Home Page Title test is FAILED ************')
            assert False

    def test_login(self, setup):

        self.logger.error('*************Verifying login test ************')
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.error('*************Login test is PASSED ************')
        else:
            self.driver.save_screenshot(r"C:\Users\Daro\PycharmProjects\nopCommerceStore\Screenshots\test_login.png")
            self.driver.close()
            self.logger.error('*************Login test is FAILED ************')
            assert False


