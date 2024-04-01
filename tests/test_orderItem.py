from Pages.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOrderItem(BaseClass):
    def test_orderItem(self):
        log = self.get_Logger()

        home_page = HomePage(self.driver)

        checkout_page = home_page.shopItems()
        log.info("getting all the items")
        products = checkout_page.products()

        i = -1

        for product in products:
            i = i + 1
            phone_name = product.text
            log.info(phone_name)
            if phone_name == "Blackberry":
                checkout_page.addButtons()[i].click()

        checkout_page.checkOutButton().click()

        confirm_page = checkout_page.checkoutItems()
        log.info("Entering country name as ind")
        confirm_page.countryNameInput().send_keys("ind")

        self.verifyLinkPresence("India")

        confirm_page.selectCountry().click()

        confirm_page.selectCheckbox().click()
        confirm_page.purchaseButton().click()
        success_message = confirm_page.successMessage().text

        log.info("Text received from application is " + success_message)
        assert " Thank you! Your order will be delivered in next few weeks" in success_message

        self.driver.get_screenshot_as_file("..//Reports//screen.png")
