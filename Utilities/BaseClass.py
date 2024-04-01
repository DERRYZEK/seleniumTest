import inspect
import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.mark.flaky(reruns=3)
@pytest.mark.usefixtures("failure", "setup")
class BaseClass:
    def get_Logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        current_time = time.strftime("%Y-%m-%d")

        log_file_name = '..\\Logs\\logfile' + current_time + '.log'

        file_handler = logging.FileHandler(log_file_name)
        formatter = logging.Formatter("%(asctime)s - %(filename)s:%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        selector = Select(locator)
        (selector.select_by_visible_text(text))
