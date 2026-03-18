from playwright.sync_api import Page
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        self.page.locator(locator).click()
    
    def fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)
    
    def get_text(self, locator: str):
        return self.page.locator(locator).inner_text()
    
