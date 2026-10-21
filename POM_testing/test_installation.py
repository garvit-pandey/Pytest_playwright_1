from playwright.sync_api import Page, expect, sync_playwright
import pytest

from POM_testing.test_get_started import GetStarted


class Installation(GetStarted):

    def __init__(self, page:Page):
        super().__init__(page)     # "run the parent's setup first"
        self.page = page

    def change_theme(self):
        # switching the website theme:
            self.page.get_by_role("button", name="Switch between dark and light mode").click()
            print('theme switched')

    def next_page(self):
        self.page.get_by_role("link", name="Writing tests").first.click()