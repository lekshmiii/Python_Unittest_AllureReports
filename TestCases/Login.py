#test methods should start with keyword test_
#use necessary decorators
from allure_commons.types import AttachmentType
from selenium import webdriver
import unittest
import xmlrunner
import time
import allure
from PageObjects.PageObjectLocators import LoginPage


class LoginTest(unittest.TestCase):

    url = "http://admin-demo.nopcommerce.com"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Safari()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls_title = cls.driver.title
        if cls_title == "Your store. Login":
            assert True
        else:
            assert False

    @allure.step("Enter credentials and Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login_method(self):
        lp = LoginPage(self.driver)
        lp.enter_username(self.username)
        lp.enter_password(self.password)
        lp.click_login()
        time.sleep(5)
        self_title = self.driver.title
        if self_title == "Dashboard / nopCommerce administration":
            assert True
            allure.attach(self.driver.get_screenshot_as_png(),name="Loggedscreen has expected title",attachment_type=AttachmentType.PNG)
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="Loggedscreen title wrong",attachment_type=AttachmentType.PNG)
            assert False

    @allure.step("skipped test")
    @allure.severity(allure.severity_level.MINOR)
    @unittest.skip("this test is skipped")
    def test_skippingtest(self):
        print("this test is skipped")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)


#python -m TestCases.Login  . use this statement to run tests as unitest test cases in different folders

#below command runs the unittest test cases as allure test cases and generates reports in results directory

#python -m pytest TestCases/Login.py --alluredir ./results

#To see the results in a browser use command "allure serve <absolute path of the "results" directory>"