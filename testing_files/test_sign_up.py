import pytest
from PageObjectModels.LoginPage import LoginPage
from PageObjectModels.SignUpPage import SingUpPage


@pytest.mark.usefixtures('setUp')
class TestLoginPage():

    def test_sing_up(self):

        Login_page = LoginPage(self.driver)
        Login_page.sing_up_link().click()

    def test_sing_up_screen(self, Data):
        self.driver.implicitly_wait(5)
        Sing_Up = SingUpPage(self.driver)
        Sing_Up.enter_first_name().send_keys(Data['FirstName'])

        Sing_Up.enter_last_name().send_keys(Data['LastName'])
        Sing_Up.enter_title().send_keys(Data['Title'])
        Sing_Up.enter_email().send_keys(Data['Email'])
        Sing_Up.enter_phone_number().send_keys(Data['Phone'])
        Sing_Up.enter_company_name().send_keys(Data['Company'])
        Sing_Up.enter_num_employees().select_by_value(Data['NumOfEmployees'])
        Sing_Up.enter_country().select_by_visible_text(Data['Country'])
        Sing_Up.enter_Language().select_by_visible_text(Data['Language'])
        Sing_Up.select_check_box().click()
        self.driver.refresh()
