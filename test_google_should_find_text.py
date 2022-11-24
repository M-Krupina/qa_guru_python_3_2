from selene.support.shared import browser
from selene import be, have

def test_positive_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene'))

def test_negative_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('trdtgdgtdggxd').press_enter()
    browser.element('[class="eqAnXb"]').should(have.text('No results'))
