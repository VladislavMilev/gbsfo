from src.base_worker.search_engine import SearchEngine
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# TODO: -----------------------------------------------------------
#       1.1 Открыть google.com
#       1.2 Сделать поиск по фразе  “gbsfo”
#       1.3 Среди всех результатов найти полное соответствие с “gbsfo”
#       1.4 Открыть линку в новой Табе ----------------------------


class GoogleSearchLocators:
    locator_google_search_field = (By.NAME, 'q')
    locator_google_search_button = (By.CLASS_NAME, 'gNO89b')
    locator_google_search_results = (By.PARTIAL_LINK_TEXT, 'gbsfo')


class Matcher(SearchEngine):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.locator_google_search_field)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(GoogleSearchLocators.locator_google_search_button, time=4).click()

    def find_and_open_link_in_new_tab(self):
        link = self.find_element(GoogleSearchLocators.locator_google_search_results, time=2)

        actions = ActionChains(self.driver)
        actions.move_to_element(link)
        actions.key_down(Keys.CONTROL)
        actions.click(link)
        actions.perform()
        return self.driver.switch_to.window(self.driver.window_handles[1])
