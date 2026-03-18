from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    
    # Locators
    TITLE = ".title"
    COMPLETE_MESSAGE = ".complete-text"
    
    def get_title(self):
        return self.get_text(self.TITLE)
    
    def get_complete_message(self):
        return self.get_text(self.COMPLETE_MESSAGE)