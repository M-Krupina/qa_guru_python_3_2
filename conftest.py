import pytest
from selene.support.shared import browser

@pytest.fixture(scope="class")
def open_browser():
    browser.config.window_height = 900
    browser.config._window_width = 1600
    browser.open('https://google.com/ncr')

    yield

    browser.quit()