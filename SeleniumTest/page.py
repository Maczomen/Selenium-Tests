from locator import *
from element import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NumberOfItems(BasePageElementWithEagerAutoFill):
    def __init__(self, locator):
        self.locator = locator

class FillTextFields(BasePageElement):
    def __init__(self, locator):
        self.locator = locator

class BasePage():
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_cart_size_right(self, number_of_things_in_cart):
        element = self.driver.find_element(*MainPageLocators.CART_SIZE)
        return str(number_of_things_in_cart) in element.text

    def click_products_button(self):
        element = self.driver.find_element(*MainPageLocators.PRODUCTS_BUTTON)
        element.click()

    def click_cart_button(self):
        element = self.driver.find_element(*MainPageLocators.CART_BUTTON)
        element.click()

    def click_sign_in_button(self):
        element = self.driver.find_element(*CartPageLocators.SIGN_IN_BUTTON)
        element.click()

    def is_logged_in(self):
        return "Wyloguj" in self.driver.page_source

class ProductsPage(BasePage):

    def click_products_category_button(self, which):
        results = self.driver.find_elements(*ProductsPageLocators.CATEGORY_BUTTONS)
        results[which].click()

    def click_home_page_button(self):
        element = self.driver.find_element(*ProductsPageLocators.HOME_PAGE_BUTTON)
        element.click()

class ProductsCategoryPage(BasePage):

    def click_product_button(self, which):
        results = self.driver.find_elements(*ProductsCategoryPageLocators.PRODUCTS_BUTTONS)
        results[which].click()

    def return_to_last_page(self):
        self.driver.back()

class ProductPage(BasePage):
    numberOfItems = NumberOfItems(ProductPageLocators.NUMBER_OF_ITEM)

    def set_number_of_items(self, how_many):
        button = self.driver.find_element(*ProductPageLocators.INCREASE_NUMBER_OF_ITEMS_BUTTON)
        for i in range(0,how_many - 1):
            button.click()

    def click_add_to_cart_button(self):
        element = self.driver.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        element.click()

    def is_present(self):
        if "Obecnie brak na stanie" in self.driver.page_source:
            return False
        return True

    def how_many(self):
        result = self.driver.find_element(*ProductPageLocators.HOW_MANY).get_attribute("data-stock")
        return int(result)


    def return_to_last_page(self):
        self.driver.back()

    def click_home_page_button(self):
        element = self.driver.find_element(*ProductPageLocators.HOME_PAGE_BUTTON)
        element.click()

    def click_continue_shopping_button(self):
        found = self.driver.find_elements(*ProductPageLocators.CART_POP_UP)
        if len(found) == 0:
            return
        element = self.driver.find_element(*ProductPageLocators.CLOSE_CART_POP_UP_BUTTON)
        element.click()



class CartPage(BasePage):

    def click_remove_from_cart_button(self, which):
        results = self.driver.find_elements(*CartPageLocators.DELETE_BUTTON)
        results[which].click()

    def is_cart_size_right(self, number_of_unique_things_in_cart):
        time.sleep(5)
        results = WebDriverWait (self.driver, 10).until(
           EC.presence_of_all_elements_located(CartPageLocators.NUMBER_OF_UNIQUE_ITEMS)) #to zmienic
        results = self.driver.find_elements(*CartPageLocators.NUMBER_OF_UNIQUE_ITEMS)
        return number_of_unique_things_in_cart == len(results)

    def click_checkout_button(self):
        element = self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON)
        element.click()

    def click_sign_in_button(self):
        element = self.driver.find_element(*CartPageLocators.SIGN_IN_BUTTON)
        element.click()

class CheckoutPage(BasePage):
    name = FillTextFields(CheckoutPageLocators.NAME_FIELD)
    surname = FillTextFields(CheckoutPageLocators.SURNAME_FIELD)
    email = FillTextFields(CheckoutPageLocators.EMAIL_FIELD)
    adress = FillTextFields(CheckoutPageLocators.ADRESS_FIELD)
    post_code = FillTextFields(CheckoutPageLocators.POST_CODE_FIELD)
    city = FillTextFields(CheckoutPageLocators.CITY_FIELD)
 
    def mark_the_gender_field(self):
        element = self.driver.find_element(*CheckoutPageLocators.GENDER_MALE_RADIO_BUTTON)
        element.click()

    def accept_terms_of_use_check_box(self):
        element = self.driver.find_element(*CheckoutPageLocators.TERMS_OF_USE_CHECK_BOX)
        element.click()

    def accept_privacy_check_box(self):
        element = self.driver.find_element(*CheckoutPageLocators.PRIVACY_CHECK_BOX)
        element.click()

    def click_personal_data_to_adress_button(self):
        element = self.driver.find_element(*CheckoutPageLocators.REGISTER_NEW_CUSTOMER_BUTTON)
        element.click()

    def click_adress_to_delivery_button(self):
        element = self.driver.find_element(*CheckoutPageLocators.CONFIRM_ADDRESS_BUTTON)
        element.click()

    def mark_delivery_type_field(self):
        element = self.driver.find_element(*CheckoutPageLocators.DELIVERY_TYPE_RADIO_BUTTON)
        element.click()

    def click_delivery_to_payment_button(self):
        element = self.driver.find_element(*CheckoutPageLocators.CONFIRM_DELIVERY_BUTTON)
        element.click()

    def accept_terms_of_payment_check_box(self):
        element = self.driver.find_element(*CheckoutPageLocators.TERMS_OF_PAYMENT_CHECK_BOX)
        element.click()

    def click_submit_order_button(self):
        element = self.driver.find_element(*CheckoutPageLocators.SUBMIT_ORDER_BUTTON)
        element.click()

    def mark_payment_option_field(self):
        element = self.driver.find_element(*CheckoutPageLocators.PAYMENT_TYPE_RADIO_BUTTON)
        element.click()


class LoginPage(BasePage):

    def click_register_new_user_link(self):
        element = self.driver.find_element(*LoginPageLocators.REGISTER_NEW_USER_LINK)
        element.click()

class RegisterPage(BasePage):
    name = FillTextFields(RegisterPageLocators.NAME_FIELD)
    surname = FillTextFields(RegisterPageLocators.SURNAME_FIELD)
    email = FillTextFields(RegisterPageLocators.EMAIL_FIELD)
    password = FillTextFields(RegisterPageLocators.PASSWORD_FIELD)
    birthDate = FillTextFields(RegisterPageLocators.BIRTH_DATE_FIELD)

    def mark_the_gender_field(self):
        element = self.driver.find_element(*RegisterPageLocators.GENDER_MALE_RADIO_BUTTON)
        element.click()

    def accept_terms_of_use_check_box(self):
        element = self.driver.find_element(*RegisterPageLocators.TERMS_OF_USE_CHECK_BOX)
        element.click()

    def accept_privacy_check_box(self):
        element = self.driver.find_element(*RegisterPageLocators.PRIVACY_CHECK_BOX)
        element.click()

    def click_register_new_user_button(self):
        element = self.driver.find_element(*RegisterPageLocators.REGISTER_NEW_CUSTOMER_BUTTON)
        element.click()

class AfterPurchasePage(BasePage):

    def is_transaction_successful(self):
        return "potwierdzone" in self.driver.page_source

    def click_home_page_button(self):
        element = self.driver.find_element(*AfterPurchasePageLocators.HOME_PAGE_BUTTON)
        element.click()

    def click_profil_link(self):
        element = self.driver.find_element(*AfterPurchasePageLocators.PROFIL_LINK)
        element.click()

class AccountPage(BasePage):

    def click_history_button(self):
        element = self.driver.find_element(*AccountPageLocators.HISTORY_BUTTON)
        element.click()

class HistoryPage(BasePage):

    def click_order_details_button(self):
        results = self.driver.find_elements(*HistoryPageLocators.ORDER_DETAILS_LINKS)
        results[0].click()

class OrderDetailsPage(BasePage):

    def is_waiting_for_payment(self):
        return "" in self.driver.page_source
