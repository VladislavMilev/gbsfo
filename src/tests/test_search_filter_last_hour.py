from selenium.webdriver.support import expected_conditions as ec
from src.pages.search_filter_last_hour import FilterSetter
from selenium.webdriver.support.wait import WebDriverWait

KEYWORD = 'gbsfo'
URL = 'https://www.google.com/'


def test_set_filter_last_hour(driver_manager):
    wait = WebDriverWait(driver_manager, 5)

    google_filter_tools = FilterSetter(driver=driver_manager, url=URL)
    google_filter_tools.go_to_search_engine()
    google_filter_tools.enter_word(KEYWORD)
    google_filter_tools.click_on_the_search_button()
    google_filter_tools.click_on_the_search_tools_button()
    google_filter_tools.click_on_the_search_time_select_button()
    google_filter_tools.locator_google_search_time_select_item()

    try:
        wait.until(ec.title_is('gbsfo - Поиск в Google'))
    finally:
        assert 'gbsfo - Поиск в Google' in driver_manager.title
