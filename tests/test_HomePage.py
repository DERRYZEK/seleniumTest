import pytest

from Pages.HomePage import HomePage
from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_HomePage(self, getData):
        log = self.get_Logger()
        home_page = HomePage(self.driver)
        log.info("Entering name")
        home_page.getName().send_keys(getData["name"])
        log.info("Entering Email")
        home_page.getEmail().send_keys(getData["email"])
        log.info("Entering password")
        home_page.getPassword().send_keys(getData["password"])
        log.info("Checkbox clicked")
        home_page.getCheckBox().click()

        log.info("Gender selected")
        self.selectOptionByText(home_page.getGender(), getData["gender"])
        home_page.getRadioButton().click()
        home_page.getSubmitButton().click()

        log.info("Application message " + home_page.getSuccessMessage().text)
        assert "Success" in home_page.getSuccessMessage().text

        self.driver.get_screenshot_as_file("..//Reports//home_screen.png")

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param
