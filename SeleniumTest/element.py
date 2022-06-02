from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class BasePageElementWithEagerAutoFill():
    """Base page class that is initialized on every page object class."""


    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).send_keys(Keys.ARROW_RIGHT + str(value) + Keys.ARROW_LEFT + Keys.BACK_SPACE)


    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")

class BasePageElement():
    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator))
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)


    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by(*self.locator))
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")