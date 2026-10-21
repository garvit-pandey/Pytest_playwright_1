from playwright.sync_api import Page, expect, sync_playwright
import pytest

from POM_testing.test_get_started import GetStarted
from POM_testing.test_installation import Installation
from POM_testing.test_writing_tests import Writing_tests
from POM_testing.test_botttom_integrations import Integrations
from POM_testing.test_search import Search


@pytest.mark.smoke
def test_other_functions(home_page: Page):

    page = Search(home_page)
    page.get_started()
    page.click_getstart()
    page.next_page()
    page.change_theme()
    page.next_page()

    
    page.current_page()
    page.change_language()

    
    page.click_integration()
    page.click_selenium_grid()


    page.goToSearch()
    page.random_input()
    page.clear_search_field()
    page.correct_input()
    page.search_clicked()

    print('test executed successfully')