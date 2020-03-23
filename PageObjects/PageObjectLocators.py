from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class LoginPage():

    username_id = "Email"
    password_id = "Password"
    login_button_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/input"


    def __init__(self,driver):
        self.driver=driver

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()