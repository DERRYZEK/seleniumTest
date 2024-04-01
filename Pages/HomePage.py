from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.CheckOutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check_box = (By.XPATH, "//input[@id='exampleCheck1']")
    drop_down = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    radio_button = (By.XPATH, "//input[@id='inlineRadio1']")
    submit_button = (By.CSS_SELECTOR, "input[value='Submit']")
    success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.check_box)

    def getGender(self):
        return self.driver.find_element(*HomePage.drop_down)

    def getRadioButton(self):
        return self.driver.find_element(*HomePage.radio_button)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit_button)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success_message)

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        return CheckOutPage(self.driver)
