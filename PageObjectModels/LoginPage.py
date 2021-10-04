from selenium.webdriver.common.by import By


class LoginPage:

    sing_up = (By.ID, 'signup_link')

    def __init__(self, driver):
        self.driver = driver

    def sing_up_link(self):
        return self.driver.find_element(*LoginPage.sing_up)
