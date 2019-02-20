from behave import *
from selenium.webdriver.common.by import *
import random

use_step_matcher("re")


@step('I open the customer Tab "(?P<type1>.+)"')
def step_impl(context, type1):
    context.browser.switch_to_frame("left_nav")
    context.browser.find_element(By.LINK_TEXT, "Customer Management").click()
    context.browser.implicitly_wait(5)
    if type1 == "add":
        context.browser.find_element(By.XPATH, "/html/body/form/table[2]/tbody/tr[2]/td/div/div[2]/ul/li[8]/ul/li/div/a").click()
        context.browser.switch_to_default_content()
        context.browser.switch_to_frame("main")
        context.browser.find_element(By.ID, "form1")
        context.browser.find_element(By.CSS_SELECTOR, "span.igtab_THTab:nth-child(2) > span:nth-child(1) > span:nth-child(1)").click()
    elif type1 == "edit":
        context.browser.find_element(By.XPATH, "/html/body/form/table[2]/tbody/tr[2]/td/div/div[2]/ul/li[8]/ul/li/div/a").click()
        context.browser.switch_to_default_content()
        context.browser.switch_to_frame("main")
        context.browser.find_element(By.ID, "form1")
    elif type1 == "delete":
        context.browser.find_element(By.XPATH, "/html/body/form/table[2]/tbody/tr[2]/td/div/div[2]/ul/li[8]/ul/li/div/a").click()
        context.browser.switch_to_default_content()
        context.browser.switch_to_frame("main")
        context.browser.find_element(By.ID, "form1")


@step('I enter a enter a new customer "(?P<nickname>.+)" and "(?P<companyName>.+)" and "(?P<first_name>.+)" and "(?P<last_name>.+)" and "(?P<routing_num>.+)" and "(?P<account_num>.+)" and "(?P<type1>.+)"')
def step_impl(context, nickname, companyName, first_name, last_name, routing_num, account_num, type1):
    context.browser.implicitly_wait(5)
    if type1 == "add":
        for x in range(10):
            y = random.randint(1, 2501)
        nick = nickname + str(y)
        context.browser.find_element(By.ID, "txtNickName").send_keys(nick)
        context.browser.find_element(By.ID, "txtCompany").send_keys(companyName)
        context.browser.find_element(By.ID, "txtFirstName").send_keys(first_name)
        context.browser.find_element(By.ID, "txtLastName").send_keys(last_name)
        context.browser.find_element(By.ID, "txtRoutingNumber").send_keys(routing_num)
        context.browser.find_element(By.ID, "txtAccountNumber").send_keys(account_num)


@step('I click the Save clerk button and "(?P<type1>.+)"')
def step_impl(context, type1):
    if type1 == "add" or type1 == "edit":
        context.browser.find_element(By.ID, "tabCustomerManagement_tmpl1_btnSave").click()


@step('I edit the customer"(?P<type1>.+)"')
def step_impl(context, type1):
    if type1 == "edit":
        context.browser.find_element(By.ID, "tabCustomerManagement_tmpl0_grdCustomerList_it0_33_ViewTransaction").click()


@step('I delete the customer "(?P<type1>.+)"')
def step_impl(context, type1):
        if type1 == "delete":
            context.browser.find_element(By.ID, "tabCustomerManagement_tmpl0_grdCustomerList_it0_33_ViewTransaction").click()
            context.browser.find_element(By.ID, "tabCustomerManagement_tmpl1_btnDelete").click()
            #context.browser.implicitly_wait(5)
            #context.browser.send_keys(u'\ue007')

            alert = context.browser.switch_to.alert
            alert.accept()
