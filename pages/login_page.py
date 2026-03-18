from pages.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"

    def enter_username(self, username):
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()