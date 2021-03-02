import pytest
from selenium import webdriver
from selenium.webdriver.android.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager  # Не люблю статические файлы в сорцах, импорт WDM удобнее


# -----------------------------------------------------------
# Для использования других браузеров:
#
# from webdriver_manager.opera import OperaDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
#
# Импортировать в фикстуру при надобности:
#
# driver: WebDriver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver: WebDriver = webdriver.Opera(executable_path=OperaDriverManager().install())
# -----------------------------------------------------------

@pytest.fixture(scope='function')  # Решил использовать драйвер 1 раз на тествовую функцию
def driver_manager():

    driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.set_window_size(1000, 800)
    yield driver
    driver.quit()
