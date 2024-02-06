from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target.com')
def Open_target_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart icon')
def Click_on_Cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()
    sleep(6)


@then('“Your cart is empty” message is shown')
def message_is_shown(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Your cart is empty')]")
    assert 'Your cart is empty' in actual_text
    print(actual_text)
    print('Test case passed')