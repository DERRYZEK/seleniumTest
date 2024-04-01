from selenium.webdriver.common.by import By


class ConfirmPage:
    country_name_input = (By.XPATH, "//input[@id='country']")
    select_country = (By.LINK_TEXT, "India")
    select_checkbox = (By.XPATH, "//label[@for='checkbox2']")
    purchase_button = (By.XPATH, "//input[@value='Purchase']")
    success_message = (By.XPATH, "(//div[@class='alert alert-success alert-dismissible'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def countryNameInput(self):
        return self.driver.find_element(*ConfirmPage.country_name_input)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.select_country)

    def selectCheckbox(self):
        return self.driver.find_element(*ConfirmPage.select_checkbox)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.success_message)
