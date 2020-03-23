# Python_Unittest_AllureReports
Using Python Unittest framework to test and generate Allure Reports

The user "admin" logs in to a website "http://admin-demo.nopcommerce.com" using credentials .
The project is an explaination on how to use Allure Reports with Unittest framework. Project has 2 directories. 
TestCase directory has module named Login.py that has test steps defined as allure steps using allure decorators.
Also screen shots are saved in allure reports as mentioned in the test steps.
The second directory is PageObjects. It has a module PageObjectLocators.py that calls all the required web elements on the Login Page


#python -m TestCases.Login  . use this statement to run tests as unitest test cases

#below command runs the unittest test cases as allure test cases and generates reports in "AllureReports" directory

#python -m pytest TestCases/Login.py --alluredir ./AllureReports

#To see the allure reports in a browser use command "allure serve <absolute path of the "AllureReports" directory>". 
You should have allure installed and "allure-pytest" package added to the project through project preferences in Pycharm
