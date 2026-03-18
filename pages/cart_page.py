from pages.base_page import BasePage

class CartPage(BasePage):

    #Locators
    TITLE = ".title"
    ITEM_NAME = ".inventory_item_name"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    CHECKOUT_BUTTON = "#checkout"

    def get_title(self):
        return self.get_text(self.TITLE)
    
    def get_cart_item_name(self):
        return self.get_text(self.ITEM_NAME)
    
    def get_cart_item_price(self):
        return self.get_text(self.ITEM_PRICE)
    
    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
