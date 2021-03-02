from src.base_worker.search_engine import SearchEngine
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


# TODO: -----------------------------------------------------------
#       2.1 Открыть google.com
#       2.2 Сделать поиск по фразе  “gbsfo”
#       2.3 Выбрать “инструменты” и внутри выбрать отображать данные только за последний час

class GoogleSearchLocators:
    locator_google_search_field = (By.NAME, 'q')
    locator_google_search_button = (By.CLASS_NAME, 'gNO89b')
    locator_google_search_tools_button = (By.CLASS_NAME, 't2vtad')
    locator_google_search_time_select_button = (By.XPATH, '//*[@id="hdtbMenus"]/span[2]')
    locator_google_search_time_select_item = (By.XPATH, '//*[@id="lb"]/div/g-menu/g-menu-item[2]')


class FilterSetter(SearchEngine):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.locator_google_search_field)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(GoogleSearchLocators.locator_google_search_button, time=5).click()

    def click_on_the_search_tools_button(self):
        button = self.find_element(GoogleSearchLocators.locator_google_search_tools_button, time=5)

        actions = ActionChains(self.driver)
        actions.move_to_element(button)
        actions.click(button)
        actions.perform()
        return button

    def click_on_the_search_time_select_button(self):
        select = self.find_element(GoogleSearchLocators.locator_google_search_time_select_button, time=5)

        actions = ActionChains(self.driver)
        actions.move_to_element(select)
        actions.click(select)
        actions.perform()
        return select

    def locator_google_search_time_select_item(self):
        return self.find_element(GoogleSearchLocators.locator_google_search_time_select_item, time=2).click()
