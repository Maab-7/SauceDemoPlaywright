from pages.base_page import BasePage

class ProductPage(BasePage):

    # Locators
    TITLE = ".title"
    CART_BUTTON = "#shopping_cart_container"

    def get_title(self):
        return self.get_text(self.TITLE)
    
    def add_to_cart(self, product_name):
        locator = f"#add-to-cart-{product_name.lower().replace(' ', '-')}"
        self.click(locator)

    def get_remove_button_text(self, product_name):
        locator = f"#remove-{product_name.lower().replace(' ', '-')}"
        return self.get_text(locator)
    
    def click_cart_button(self):
        self.click(self.CART_BUTTON)

    def get_item_price(self, product_name):
        locator = f"//button[@id='add-to-cart-{product_name.lower().replace(' ', '-')}']" \
                  f"/ancestor::div[@class='inventory_item']//div[@class='inventory_item_price']"
        return self.page.locator(locator).inner_text()