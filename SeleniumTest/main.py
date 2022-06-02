import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page
import time
from locator import *
import random


class PythonOrgTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = Service(r'ChromeDriver\chromedriver.exe')

        self.driver = webdriver.Chrome(service=service , options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:17560/")


    def testShopping(self):
        main_page = page.MainPage(self.driver)
        

        #Adding things to cart
        number_of_things_in_cart = 0
        number_of_unique_things_in_cart = 0
        products_page = page.ProductsPage(self.driver)
        for category_number in range(3,5):
            i = 0
            product_number = 1
            while i < 2:
                main_page.click_products_button()
                products_page.click_products_category_button(category_number)

                products_category_page = page.ProductsCategoryPage(self.driver)
                products_category_page.click_product_button(product_number)

                product_page = page.ProductPage(self.driver)
                if product_page.is_present():
                    how_many = 1
                    if product_page.how_many() > 1:
                        how_many = product_page.how_many()
                        if how_many > 10:
                            how_many = 10
                        how_many = random.randint(1, how_many)
                    product_page.set_number_of_items(how_many)
                    number_of_things_in_cart += how_many
                    number_of_unique_things_in_cart += 1
                    i += 1

                    product_page.click_add_to_cart_button()
                    product_page.click_continue_shopping_button()
                product_number += 1
                product_page.click_home_page_button()

        products_page.click_home_page_button()

        assert main_page.is_cart_size_right(number_of_things_in_cart)

        #Removing item from cart
        main_page.click_cart_button()

        cart_page = page.CartPage(self.driver)
        cart_page.click_remove_from_cart_button(1)
        number_of_unique_things_in_cart -= 1

        assert cart_page.is_cart_size_right(number_of_unique_things_in_cart)

        #Registration of new account
        cart_page.click_sign_in_button()
        
        loginPage = page.LoginPage(self.driver)
        loginPage.click_register_new_user_link()

        register_page = page.RegisterPage(self.driver)
        register_page.mark_the_gender_field()
        register_page.name = "TestName"
        register_page.surname = "TestSurname"
        register_page.email = "TestEmail@email.email" + str(random.randint(0,111111111))
        register_page.password = "TestPassword"
        register_page.accept_terms_of_use_check_box()
        register_page.accept_privacy_check_box()
        register_page.click_register_new_user_button()

        assert main_page.is_logged_in()

        #Payment process
        main_page.click_cart_button()
        cart_page.click_checkout_button()

        checkout_page = page.CheckoutPage(self.driver)
        #checkout_page.mark_the_gender_field()
        #checkout_page.name = "TestName"
        #checkout_page.surname = "TestSurname"
        #checkout_page.email = "TestEmail@email.email"
        #checkout_page.accept_terms_of_use_check_box()
        #checkout_page.accept_privacy_check_box()
        #checkout_page.click_personal_data_to_adress_button()

        checkout_page.adress = "TestAdress"
        checkout_page.post_code = "11-111"
        checkout_page.city = "TestCity"
        checkout_page.click_adress_to_delivery_button()

        #Choosing delivery option
        checkout_page.mark_delivery_type_field()
        checkout_page.click_delivery_to_payment_button()

        #Choosing payment type
        checkout_page.mark_payment_option_field()

        #Confirming order
        checkout_page.accept_terms_of_payment_check_box()
        checkout_page.click_submit_order_button()

        after_purchase_page = page.AfterPurchasePage(self.driver)
        assert after_purchase_page.is_transaction_successful()

        #Inspectiong order information
        after_purchase_page.click_profil_link()

        account_page = page.AccountPage(self.driver)
        account_page.click_history_button()

        history_page = page.HistoryPage(self.driver)
        history_page.click_order_details_button()

        order_details_page = page.OrderDetailsPage(self.driver)
        assert order_details_page.is_waiting_for_payment()

        #
        input("Press Enter to continue...")






    def tearDown(self):
        self.driver.quit();

if __name__ == "__main__":
    unittest.main()