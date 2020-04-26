from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("
browser.get('https://www.instagram.com/')
sleep(5)

browser.close()
