from pages.base_page import BasePage

class CheckoutPage(BasePage):
    
    # Locators
    TITLE = ".title"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    ZIP_CODE = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    
    def get_title(self):
        return self.get_text(self.TITLE)
    
    def enter_firstname(self, firstname):
        self.fill(self.FIRST_NAME, firstname)
    
    def enter_lastname(self, lastname):
        self.fill(self.LAST_NAME, lastname)
    
    def enter_zipcode(self, zipcode):
        self.fill(self.ZIP_CODE, zipcode)
    
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)