from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target web page')
def Open_target_web(context):
    context.driver.get('https://www.target.com/')


@then('Click Sign in')
def Click_Sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
    sleep(6)

@when('click Sign In right side navigation menudir')
def Sign_In_right_side_menu(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span").click()
    sleep(5)

@then('Sign In form opened')
def Sign_In_form_opened(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class,'styles__AuthHeading')]").text
    assert 'Sign into your Target account' in actual_text

    print(actual_text)

    print('test case passed!')