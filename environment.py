
from selenium import webdriver
import uuid
import os
import platform

user = os.getenv('username')
#user = user.replace('.', '-')
mn = os.getenv('COMPUTERNAME')
os1 = platform.system()
#rel = platform.release()

tp = uuid.uuid4().int & (1 << 32)-1
print(tp)

cycle = (str(user) + '-' + str(os1) + '-' + str(mn) + '-' + str(tp))
print(cycle)


def before_feature(context, feature):
    url4 = 'http://localhost:4567/createtestcycle/'
    url3 = (url4 + str(cycle) + '/' + 'Firefox')
    print(url3 + "\n")

    context.browser = webdriver.Firefox()
    context.browser.get(url3)
    context.browser.implicitly_wait(10)
    context.browser.close()

    url5 = 'http://localhost:4567/updatetestcyclestatus/ET-727/'
    url6 = (url5 + str(cycle) + "/" + 'Start')
    print(url6 + "\n")

    context.browser = webdriver.Firefox()
    context.browser.get(url6)
    context.browser.implicitly_wait(10)
    context.browser.close()


def after_scenario(context, scenario):
    url2 = 'http://localhost:4567/updatetestcyclerun/ET-727/'
    name = scenario.name
    name = name.split()
    tc = name[0]

    if scenario.status == 'passed':
        result = 'Passed'
    elif scenario.status == 'failed':
        result = 'Failed'
    else:
        result = 'Blocked'

    url1 = (url2 + str(cycle) + '/' + tc + "/" + result + '/' + 'Completed')
    print(url1 + "\n")

    context.browser = webdriver.Firefox()
    context.browser.get(url1)
    context.browser.implicitly_wait(10)
    context.browser.close()


def after_feature(context, feature):
    print(feature.name)
    if feature.name == 'Virtual Terminal Gift':
        url5 = 'http://localhost:4567/updatetestcyclestatus/'
        url6 = (url5 + str(cycle) + "/" + 'Complete')
        print(url6 + "\n")

        context.browser = webdriver.Firefox()
        context.browser.get(url6)
        context.browser.implicitly_wait(10)
        context.browser.close()

