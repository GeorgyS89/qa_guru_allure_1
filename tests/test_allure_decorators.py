import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser


@allure.tag('trivial')
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'Georgy')
@allure.feature('Issues in repo')
@allure.story('Find a particular issue')
@allure.link('https://github.com/GeorgyS89/qa_guru_allure_1/issues', name='Repo')
def test_issue():
    open_git()
    search_repo()
    nav_to_tab()
    find_particular_issue()


@allure.step('Open GitHub')
def open_git():
    browser.open('https://github.com')


@allure.step('Search for a repo')
def search_repo():
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('GeorgyS89/qa_guru_allure_1')
    browser.element('.header-search-input').submit()


@allure.step('Navigate to Issues tab in the repo')
def nav_to_tab():
    browser.element(by.link_text('GeorgyS89/qa_guru_allure_1')).click()
    browser.element('#issues-tab').click()


@allure.step('Find a particular issue by name')
def find_particular_issue():
    browser.element(by.partial_text('Whatever')).should(be.visible)
