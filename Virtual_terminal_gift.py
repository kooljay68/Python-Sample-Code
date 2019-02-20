from behave import *
from nose.tools import assert_true, assert_is_not, assert_in
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

use_step_matcher("re")


@step("I open the Virtual Terminal Gift Form")
def step_impl(context):
    context.browser.switch_to_frame("left_nav")
    context.browser.find_element(By.LINK_TEXT, "Sale").click()
    context.browser.find_element(By.LINK_TEXT, "SPS EFT Test Merchant (C | GETI G | GETI L)").click()
    context.browser.find_element(By.LINK_TEXT, "Location 2 (GETI G | GETI L)").click()
    context.browser.find_element(By.PARTIAL_LINK_TEXT, "Virtual Terminal Gift (1032553)").click()
    context.browser.implicitly_wait(5)
    context.browser.switch_to_default_content()
    context.browser.switch_to_frame("main")


@step("I click the Key In method")
def step_impl(context):
    context.browser.find_element(By.ID, "btnNewWebTrans").click()


@step("I fill in all required form information for GiftCard_BalanceInquiry")
def step_impl(context):
    context.browser.find_element(By.ID, "txtFirstCardNumber").click()
    context.browser.find_element(By.ID, "txtFirstCardNumber").send_keys("93000000000001")


@step('I print the test "(?P<name>.+)"')
def step_impl(context, name):
    print(name)


@step('I select the profile "(?P<profile>.+)"')
def step_impl(context, profile):
    frame = context.browser.find_element(By.XPATH, "/html/body/form/div[3]/div/div[1]/iframe")
    context.browser.switch_to_frame(frame)
    trans = Select(context.browser.find_element(By.ID, "DDLProfileMapping"))
    trans.select_by_visible_text(profile)


@step('I select the transaction "(?P<transaction>.+)"')
def step_impl(context, transaction):
    trans = Select(context.browser.find_element(By.ID, "DDLTransMapping"))
    trans.select_by_visible_text(transaction)


@step('I enter the card number "(?P<card_num_true>.+)" and "(?P<card_num>.+)"')
def step_impl(context, card_num_true, card_num):
    if card_num_true == "true":
        context.browser.find_element(By.ID, "txtFirstCardNumber").click()
        context.browser.find_element(By.ID, "txtFirstCardNumber").send_keys(card_num)
        context.browser.implicitly_wait(2)
    elif card_num_true == "false":
        print("do not use card number")
        context.browser.implicitly_wait(2)


@step('I enter the transfer card "(?P<trans_card_true>.+)" and "(?P<trans_card_number>.+)"')
def step_impl(context, trans_card_true, trans_card_number):
    if trans_card_true == "true":
        context.browser.find_element(By.ID, "txtLastCardNumber").click()
        context.browser.find_element(By.ID, "txtLastCardNumber").send_keys(trans_card_number)
        context.browser.implicitly_wait(2)
    elif trans_card_true == "false":
        print("do not use transfer card number")
        context.browser.implicitly_wait(2)


@step('I enter the phone number "(?P<phone_num_true>.+)" and "(?P<phone>.+)"')
def step_impl(context, phone_num_true, phone):
    if phone_num_true == "true":
        context.browser.find_element(By.ID, "txtPhoneNumber").click()
        context.browser.find_element(By.ID, "txtPhoneNumber").send_keys(phone)
        context.browser.implicitly_wait(2)
    elif phone_num_true == "false":
        print("do not use phone")
        context.browser.implicitly_wait(2)


@step('I enter the amount "(?P<amount_true>.+)" and "(?P<amount>.+)"')
def step_impl(context, amount_true, amount):
    if amount_true == "true":
        context.browser.find_element(By.ID, "txtAmount").click()
        context.browser.find_element(By.ID, "txtAmount").send_keys(amount)
        context.browser.implicitly_wait(2)
    elif amount_true == "false":
        print("do not use amount")
        context.browser.implicitly_wait(2)


@step('I enter the required field "(?P<text>.+)"')
def step_impl(context, text):
    context.browser.find_element(By.ID, "txtCustom1").click()
    context.browser.find_element(By.ID, "txtCustom1").send_keys(text)


@then("I Submit the form")
def step_impl(context):
    context.browser.find_element(By.ID, "btnSubmit").click()


@step('I Check the "(?P<response>.+)"')
def step_impl(context, response):
    context.browser.implicitly_wait(5)
    r = context.browser.page_source
    assert_true(response in r)


@step('I enter the a void "(?P<void_true>.+)" and "(?P<void_code>.+)"')
def step_impl(context, void_true, void_code):
    if void_true == "true":
        context.browser.find_element(By.ID, "txtResponseID").click()
        context.browser.find_element(By.ID, "txtResponseID").send_keys(void_code)
        context.browser.implicitly_wait(2)
    elif void_true == "false":
        print("do not use void")
        context.browser.implicitly_wait(2)