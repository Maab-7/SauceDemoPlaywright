from pages.base_page import BasePage

class CheckoutTwoPage(BasePage):
    
    # Locators
    TITLE = ".title"
    FINISH_BUTTON = "#finish"
    ITEM_NAME = ".inventory_item_name"
    ITEM_PRICE = ".inventory_item_price"
    ITEM_TOTAL = ".summary_subtotal_label"
    TAX = ".summary_tax_label"
    TOTAL = ".summary_total_label"
    
    def get_title(self):
        return self.get_text(self.TITLE)
    
    def get_item_name(self):
        return self.get_text(self.ITEM_NAME)
    
    def get_item_price(self):
        return self.get_text(self.ITEM_PRICE)
    
    def click_finish(self):
        self.click(self.FINISH_BUTTON)
    
    def _extract_amount(self, text):
        import re
        return float(re.sub(r"[^0-9.]", "", text))
    
    def get_item_total_amount(self):
        return self._extract_amount(self.get_text(self.ITEM_TOTAL))
    
    def get_tax_amount(self):
        return self._extract_amount(self.get_text(self.TAX))
    
    def get_total_amount(self):
        return self._extract_amount(self.get_text(self.TOTAL))