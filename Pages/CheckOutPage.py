from selenium.webdriver.common.by import By

from Pages.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    products_list = (By.CSS_SELECTOR, ".card-title a")

    add_buttons = (By.CSS_SELECTOR, ".card-footer button")

    check_out_button = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    check_out_items = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    def products(self):
        return self.driver.find_elements(*CheckOutPage.products_list)

    def addButtons(self):
        return self.driver.find_elements(*CheckOutPage.add_buttons)

    def checkOutButton(self):
        return self.driver.find_element(*CheckOutPage.check_out_button)

    def checkoutItems(self):
        self.driver.find_element(*CheckOutPage.check_out_items).click()
        return ConfirmPage(self.driver)

