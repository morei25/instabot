from time import sleep
from selenium import webdriver

class LoginPage:
    def __init__(self, browser):
        self.browser = browser
    
    def login(self, username, password):
        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys("danielmoreira.dm49@gmail.com")
        password_input.send_keys("DerBot25")
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser =browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        self.browser.find_element_by_xpath("//a[text()='Login in']").click()
        sleep(3)
        return LoginPage(self.browser)

def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("danielmoreira.dm49@gmail.com","DerBot25")
    
    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

