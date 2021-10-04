from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SingUpPage:
    FirstName = (By.NAME, 'UserFirstName')
    LastName = (By.NAME, 'UserLastName')
    UserTitle = (By.NAME, 'UserTitle')
    UserEmail = (By.NAME, 'UserEmail')
    UserPhone = (By.NAME, 'UserPhone')
    UserCompany = (By.NAME, 'CompanyName')
    CompanyEmployees = (By.NAME, 'CompanyEmployees')
    Country = (By.NAME, 'CompanyCountry')
    Language = (By.NAME, 'CompanyLanguage')
    CheckBox = (By.XPATH, '//div[@class="field"]/div[1]')

    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self):
        return self.driver.find_element(*SingUpPage.FirstName)

    def enter_last_name(self):
        return self.driver.find_element(*SingUpPage.LastName)

    def enter_title(self):
        return self.driver.find_element(*SingUpPage.UserTitle)

    def enter_email(self):
        return self.driver.find_element(*SingUpPage.UserEmail)

    def enter_phone_number(self):
        return self.driver.find_element(*SingUpPage.UserPhone)

    def enter_company_name(self):
        return self.driver.find_element(*SingUpPage.UserCompany)

    def enter_num_employees(self):
        return Select(self.driver.find_element(*SingUpPage.CompanyEmployees))

    def enter_country(self):
        return Select(self.driver.find_element(*SingUpPage.Country))

    def enter_Language(self):
        return Select(self.driver.find_element(*SingUpPage.Language))

    def select_check_box(self):
        return self.driver.find_element(*SingUpPage.CheckBox)
