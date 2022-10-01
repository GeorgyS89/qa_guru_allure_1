import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser


def test_find_issue_by_name():
    allure.dynamic.tag('minor')
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.label('owner', 'Georgy')
    allure.dynamic.feature('List of issues in repo')
    allure.dynamic.story('Check for a particular issue')
    allure.dynamic.link('https://github.com/GeorgyS89/qa_guru_allure_1/issues', name='Repo')

    with allure.step('Open GitHub'):
        browser.open('https://github.com')
    with allure.step('Search for a Repo'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('GeorgyS89/qa_guru_allure_1')
        browser.element('.header-search-input').submit()
    with allure.step('Finding "Issues" tab in the repo'):
        browser.element(by.link_text('GeorgyS89/qa_guru_allure_1')).click()
        browser.element('#issues-tab').click()
    with allure.step('Find a particular issue by name'):
        browser.element(by.partial_text('Whatever')).should(be.visible)