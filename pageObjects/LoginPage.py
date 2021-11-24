from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_css = 'body > div.master-wrapper-page > div > div > div > div > div.page-body >' \
                       ' div.customer-blocks > div > form > div.buttons > button'
    link_logout_xpath = '/html[1]/body[1]/div[3]/nav[1]/div[1]/ul[1]/li[3]/a[1]'


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login_css).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()