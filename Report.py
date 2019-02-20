from behave import *
from nose.tools import assert_true, assert_is_not, assert_in
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

use_step_matcher("re")


@step("I open the Reports Tab")
def step_impl(context):
    context.browser.switch_to_frame("left_nav")
    context.browser.find_element(By.LINK_TEXT, "Reports").click()


@step('I print the report test "(?P<report_name>.+)"')
def step_impl(context, report_name):
    print(report_name)


@step('I select the report by "(?P<report_name>.+)"')
def step_impl(context, report_name):
    if report_name == "Gift & Loyalty Store Reconciliation":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Gift & Loyalty Store").click()
    elif report_name == 'Gift & Loyalty Aging/Expiration Report':
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Gift & Loyalty Aging").click()
    elif report_name == "Discount Provided Summary":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Discount Provided Summary").click()
    elif report_name == "Discount Provided Detail":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Discount Provided Detail").click()
    elif report_name == "Shop Local Reconciliation Details":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Shop Local Reconciliation Details").click()
    elif report_name == "Shop Local Reconciliation Summary":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Shop Local Reconciliation Summary").click()
    elif report_name == "Loyalty Transaction Points Detail":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Loyalty Transaction Points Detail").click()
    elif report_name == "Loyalty Transaction Points Summary":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Loyalty Transaction Points Summary").click()
    elif report_name == "Loyalty Transaction Points Averages":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Loyalty Transaction Points Averages").click()
    elif report_name == "Gift & Loyalty Customer Registration":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Gift & Loyalty Customer Registration").click()
    elif report_name == "Gift & Loyalty Clerk Transaction Detail":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Gift & Loyalty Clerk Transaction Detail").click()
    elif report_name == "Gift & Loyalty Clerk Transaction Summary":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Gift & Loyalty Clerk Transaction Summary").click()
    elif report_name == "Gift & Loyalty Transaction Detail":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Gift & Loyalty Transaction Detail").click()
    elif report_name == "Gift & Loyalty Transaction Summary":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Gift & Loyalty Transaction Summary").click()
    elif report_name == "Gift & Loyalty Transaction Averages":
        context.browser.find_element(By.PARTIAL_LINK_TEXT, "Gift & Loyalty Transaction Averages").click()
    else:
        print("Report Not Found")


@step('I enter the transactions "(?P<from1>.+)" and "(?P<from_true>.+)" and "(?P<test_type>.+)"')
def step_impl(context, from1, from_true, test_type):
    context.browser.implicitly_wait(5)
    context.browser.switch_to_default_content()
    context.browser.switch_to_frame("main")
    context.browser.find_element(By.ID, "form1")
    if test_type == "0":
        if from_true == "true":
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte4 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte4 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").send_keys(from1)
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte4 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.implicitly_wait(2)
        elif from_true == "false":
            print("do not use transactions from")
            context.browser.implicitly_wait(2)
    elif test_type == "1":
        if from_true == "true":
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte3 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte3 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").send_keys(from1)
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte3 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.implicitly_wait(2)
        elif from_true == "false":
            print("do not use transactions from")
            context.browser.implicitly_wait(2)
    elif test_type == "2":
        if from_true == "true":
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte6 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte6 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").send_keys(from1)
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte6 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.implicitly_wait(2)
        elif from_true == "false":
            print("do not use transactions from")
            context.browser.implicitly_wait(2)
    elif test_type == '3':
        if from_true == "true":
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte5 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte5 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").send_keys(from1)
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte5 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.implicitly_wait(2)
        elif from_true == "false":
            print("do not use transactions from")
            context.browser.implicitly_wait(2)


@step('I enter a clerk ID "(?P<clerk_id>.+)" and "(?P<clerk_id_true>.+)" and "(?P<test_type>.+)"')
def step_impl(context, clerk_id, clerk_id_true, test_type):
    if test_type == "3":
        if clerk_id_true == "true":
            context.browser.find_element(By.ID, "MainTab_tmpl0_txtGetList7").click()
            context.browser.find_element(By.ID, "MainTab_tmpl0_txtGetList7").send_keys(clerk_id)
            context.browser.implicitly_wait(2)
        elif clerk_id_true == "false":
            print("do not Clerk Id")
            context.browser.implicitly_wait(2)


@then("I click view report")
def step_impl(context):
    context.browser.find_element(By.ID, "MainTab_tmpl0_btnSubmit").click()


@step('I check the number of "(?P<rows>.+)"')
def step_impl(context, rows):
    context.browser.implicitly_wait(5)
    r = context.browser.page_source
    assert_true(rows in r)


@step('I select the filter "(?P<filter_type>.+)" and "(?P<filter_true>.+)" and "(?P<test_type>.+)"')
def step_impl(context, filter_type, filter_true, test_type):
    if test_type == "0":
        if filter_true == "true":
            context.browser.find_element(By.ID, "MainTab_tmpl0_cboValue6").click()
            context.browser.find_element(By.ID, "MainTab_tmpl0_cboValue6").send_keys(filter_type)
            context.browser.implicitly_wait(2)
        elif filter_true == "false":
            print("Use Default Filter")
            context.browser.implicitly_wait(2)


@step('I enter the transactions to "(?P<to>.+)" and "(?P<to_true>.+)" and "(?P<test_type>.+)"')
def step_impl(context, to, to_true, test_type):
    if test_type == "0":
        if to_true == "true":
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte5 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte5 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").send_keys(to)
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte5 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.implicitly_wait(2)
        elif to_true == "false":
            print("do not use transactions from")
            context.browser.implicitly_wait(2)
    elif test_type == '1':
        if to_true == "true":
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte4 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte4 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").send_keys(to)
            context.browser.find_element(By.CSS_SELECTOR, "#MainTab_tmpl0_dte4 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.implicitly_wait(2)
        elif to_true == "false":
            print("do not use transactions from")
            context.browser.implicitly_wait(2)
    elif test_type == '2':
        if to_true == "true":
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte7 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte7 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").send_keys(to)
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte7 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.implicitly_wait(2)
        elif to_true == "false":
            print("do not use transactions from")
            context.browser.implicitly_wait(2)
    elif test_type == '3':
        if to_true == "true":
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte6 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte6 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)").send_keys(to)
            context.browser.find_element(By.CSS_SELECTOR,"#MainTab_tmpl0_dte6 > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)").click()
            context.browser.implicitly_wait(2)
        elif to_true == "false":
            print("do not use transactions from")
            context.browser.implicitly_wait(2)

