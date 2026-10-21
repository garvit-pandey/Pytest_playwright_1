from playwright.sync_api import Page, expect, sync_playwright
import pytest

from POM_testing.test_writing_tests import Writing_tests

class Integrations(Writing_tests):

    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

    def click_integration(self):
        self.page.get_by_title('Integrations', exact=True).click()

    def click_selenium_grid(self):
        self.page.get_by_text('Selenium Grid (experimental)').click()
        self.page.wait_for_timeout(3000)
        print(self.page.locator('h1').first.inner_text())
