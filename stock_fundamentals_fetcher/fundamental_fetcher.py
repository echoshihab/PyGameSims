from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


chrome_driver_path = "C:\selenium_drivers\chromedriver.exe"

# go to finance page
resource_page = "https://ca.finance.yahoo.com/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(resource_page)

# log in to get related news about your portfolia
time.sleep(4)
driver.find_element_by_id("uh-signedin").click()
time.sleep(4)
driver.find_element_by_id("login-username").send_keys("youremail@yahoo.com")
driver.find_element_by_id("login-signin").click()
time.sleep(4)
driver.find_element_by_id("login-passwd").send_keys("yourpassword")
driver.find_element_by_id("login-signin").click()

time.sleep(3)

#select watchlist from dropdown
action = ActionChains(driver)
hover_element = driver.find_element_by_css_selector('a[title="My Portfolio"]')
action.move_to_element(hover_element).perform()
driver.find_element_by_css_selector('a[title="My Watchlist"]').click()
time.sleep(3)

#find and print article titles
articles = driver.find_element_by_class_name("article-cluster-boundary")
headline_articles = articles.find_elements_by_css_selector("li[class='Mb(15px)']")
headlines = []

for item in headline_articles:
    item.find_element_by_tag_name("h3")
    headlines.append(item)

for index in range(len(headlines)):
    print(headlines[index].text)
    print('\n')






