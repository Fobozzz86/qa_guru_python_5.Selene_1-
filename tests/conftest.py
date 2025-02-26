import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)

def browser_management():
    browser.config.driver_name = 'edge'
    browser.config.base_url = 'https://todomvc.com/examples/emberjs'


    yield # передает управление тесту

    browser.quit()