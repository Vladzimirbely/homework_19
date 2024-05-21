from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser


def test_search():
    with step('Press Skip button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Type search'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Android')
