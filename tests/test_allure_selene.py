from selene import by,be
from selene.support.shared import browser


def test_selene_allure():
    browser.open('https://github.com')
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('GeorgyS89/qa_guru_allure_1')
    browser.element('.header-search-input').submit()
    browser.element(by.link_text('GeorgyS89/qa_guru_allure_1')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('Whatever')).should(be.visible)