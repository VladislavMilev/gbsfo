from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from src.pages.match_gbsfo_link import Matcher
import pytest


KEYWORD = 'gbsfo'
URL = 'https://www.google.com/'


@pytest.mark.xfail
def test_gbsfo_link(driver_manager):
    wait = WebDriverWait(driver_manager, 5)

    google_search_link = Matcher(driver=driver_manager, url=URL)
    google_search_link.go_to_search_engine()
    google_search_link.enter_word(KEYWORD)
    google_search_link.click_on_the_search_button()
    google_search_link.find_and_open_link_in_new_tab()

    try:
        wait.until(ec.title_is('GBSFO'))
    finally:
        assert 'GBSFO2' in driver_manager.title
        assert wait.until(ec.new_window_is_opened)


def test_linkedin_link(driver_manager):
    wait = WebDriverWait(driver_manager, 5)

    google_search_link = Matcher(driver=driver_manager, url='https://www.google.com/')
    google_search_link.go_to_search_engine()
    google_search_link.enter_word(KEYWORD)
    google_search_link.click_on_the_search_button()
    google_search_link.find_and_open_link_in_new_tab()

    try:
        wait.until(ec.title_is('GBSFO | Custom Software Solutions Provider | LinkedIn'))
    finally:
        assert 'LinkedIn' in driver_manager.title
        assert wait.until(ec.new_window_is_opened)
