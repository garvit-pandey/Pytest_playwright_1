from playwright.sync_api import Page, expect


class GetStarted:

    def __init__(self, page: Page):
        self.page = page
        

    def get_started(self):
        print(self.page.locator('h1').first.inner_text())

    def click_getstart(self):
        self.page.get_by_role("link", name="Get started").click()
        self.page.wait_for_timeout(2000)

    def next_page(self):
        expect(self.page.get_by_role("heading", name="Installation")).to_be_visible()
