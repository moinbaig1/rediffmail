import time
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('Launch Chrome browser')
def launchbrowser(context):
       context.driver=webdriver.Chrome()

@when('open rediffmail login page')
def openrediff(context):
    context.driver.get("https://mypage.rediff.com/login/dologin")

@then('Enter username "{user}" invalid password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.ID,"txtlogin").send_keys(user)
    context.driver.find_element(By.ID,"pass_box").send_keys(pwd)

@then('Enter username "{user}" valid password "{pwd}"')
def step_impl(context,user,pwd):
    context.driver.find_element(By.ID,"txtlogin").send_keys(user)
    context.driver.find_element(By.ID,"pass_box").send_keys(pwd)

@then('submit')
def step_login(context):
    context.driver.find_element(By.XPATH, "//*[@id='pass_div']/input[3]").click()
    time.sleep(5)

@then('display not valid')
def displayfailed(context):
    context.driver.find_element(By.CLASS_NAME, "errmsg")
# test comment
@then('display valid')
def displayfailed(context):
    linkelement = context.driver.find_element(By.XPATH, '//*[@id="signin_info"]/a')

