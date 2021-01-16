from selenium import webdriver

edge_browser = webdriver.Edge("./msedgedriver")

edge_browser.maximize_window()
edge_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

user_message = edge_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys("BJORN IRONSIDE")

show_message_button = edge_browser.find_element_by_class_name("btn-default")
show_message_button.click()

output_message = edge_browser.find_element_by_id('display')

assert "BJORN IRONSIDE" in output_message.text 

edge_browser.close()