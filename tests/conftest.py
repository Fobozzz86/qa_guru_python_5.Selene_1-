import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)

# Всего есть пять уровней:
#
# «function» — для функции (по умолчанию).
# «class» — для класса.
# «module» — для модуля (то есть py-файла).
# «package» — для пакета.
# «session» — для всей сессии тестирования.
# Выбор уровня фикстуры зависит от её назначения:
#
# Scope='function' — когда нужна инициализация каждый раз перед тестом.
# Scope='module' — когда нужна инициализация один раз для всех тестов в модуле.
# Scope='session' — один раз для всей сессии тестирования.
# Scope='class' — когда нужна инициализация один раз для всех тестов в классе.

def browser_management():
    browser.config.driver_name = 'edge'
    browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    # browser.config.timeout = 2.0
    # browser.config.type_by_js = True # ввод в поле через JavaScript (быстрее без симуляции по каждой букве)

    # driver_options = webdriver.FirefoxOptions()
    '''
    ↑ if we would want to use Firefox with custom browser options instead of Chrome
    '''
    driver_options = webdriver.ChromeOptions()
    #driver_options.add_argument('--headless') # запуск браузера в невидимом режиме

    # browser.config.driver = webdriver.Chrome(
    #     service=ChromeService(executable_path=ChromeDriverManager().install()),
    #     options=driver_options,
    # )
    # ↑ однажды нам понадобится что-то подобное для какой-нибудь сложной настройки браузера
    # или поддержки какого-нибудь конкретного браузера или драйвера
    # ↓ но пока достаточно просто передать параметры драйвера в конфигурацию Selene

    browser.config.driver_options = driver_options

    yield # передает управление тесту

    browser.quit()