from playwright.sync_api import expect

from POM_testing.test_botttom_integrations import Integrations


random_txt = '1234'
new_value = 'Actions'

class Search(Integrations):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def goToSearch(self):
        self.page.get_by_role('button', name='search').click()
        print('search')

    def random_input(self):
        search_bar = self.page.locator('#docsearch-input')
        search_bar.press_sequentially(random_txt, delay=100)
        print('entered the text randome text')
        self.page.wait_for_timeout(2000)

    def clear_search_field(self):
        self.page.locator('.DocSearch-Clear').click()
        print('cleared the garbage input')
        # page.wait_for_timeout(5000)

    def correct_input(self):
        search_bar = self.page.locator('#docsearch-input')
        search_bar.press_sequentially(new_value, delay=100)
        print('entered the text as Actions')

    def search_clicked(self):
        search_bar = self.page.locator('#docsearch-input')
        search_bar.press('Enter')
        print('entered text and pressed enter')
        self.page.wait_for_timeout(4000)
        print(self.page.locator('h1').first.inner_text())
        self.page.wait_for_timeout(2000)
