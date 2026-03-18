import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_two_page import CheckoutTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

PRODUCT_NAME = "Sauce Labs Onesie"

def test_login_success(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.login("standard_user", "secret_sauce")
    assert product_page.get_title() == "Products", f"Título incorrecto: {product_page.get_title()}"


def test_e2e(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    checkout_two_page = CheckoutTwoPage(page)
    checkout_complete_page = CheckoutCompletePage(page)

    # Login
    login_page.login("standard_user", "secret_sauce")
    assert product_page.get_title() == "Products"

    # Agregar al carrito
    item_price = product_page.get_item_price(PRODUCT_NAME)
    product_page.add_to_cart(PRODUCT_NAME)
    assert product_page.get_remove_button_text(PRODUCT_NAME) == "Remove"

    # Carrito
    product_page.click_cart_button()
    assert cart_page.get_title() == "Your Cart"
    assert cart_page.get_cart_item_name() == PRODUCT_NAME
    assert cart_page.get_cart_item_price() == item_price

    # Checkout
    cart_page.click_checkout()
    assert checkout_page.get_title() == "Checkout: Your Information"
    checkout_page.enter_firstname("Marco")
    checkout_page.enter_lastname("Alfaro")
    checkout_page.enter_zipcode("00000")
    checkout_page.click_continue()

    # Checkout overview
    assert checkout_two_page.get_title() == "Checkout: Overview"
    assert checkout_two_page.get_item_name() == PRODUCT_NAME
    assert checkout_two_page.get_item_price() == item_price

    subtotal = checkout_two_page.get_item_total_amount()
    tax = checkout_two_page.get_tax_amount()
    total = checkout_two_page.get_total_amount()
    assert abs(total - (subtotal + tax)) < 0.01, \
        f"Total incorrecto. Subtotal={subtotal} Tax={tax} Total={total}"

    # Finalizar
    checkout_two_page.click_finish()
    assert checkout_complete_page.get_title() == "Checkout: Complete!"
    assert checkout_complete_page.get_complete_message() == \
        "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
    