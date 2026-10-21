from playwright.sync_api import expect, Page
import pytest
from POM_testing.test_installation import Installation


class Writing_tests(Installation):

    def __init__(self, page: Page):
        super().__init__(page)     # "run the parent's setup first"

    def current_page(self):
        expect(self.page.get_by_role('heading', name="Writing tests")).to_be_visible()

    def change_language(self):
        self.page.get_by_role("button", name="Python").click()
        self.page.wait_for_timeout(3000)
        self.page.get_by_role("link", name="Java", exact=True).click()
        self.page.wait_for_timeout(3000)
        print('switched to Java')