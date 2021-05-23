from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\selenium_drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/home")

#click sign in
driver.find_element_by_link_text("Sign in").click()

#enter username
username = driver.find_element_by_id("username")
username.send_keys("yourusername")

#enter password
password = driver.find_element_by_id("password")
password.send_keys("yourpassword")

#click submit button
driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()

#click on jobs
driver.find_element_by_id('ember21').click()

#select searchbox
driver.find_element_by_id("jobs-search-box-keyword-id-ember38").send_keys("python")

#select location
location = driver.find_element_by_id("jobs-search-box-location-id-ember613")

location.send_keys("remote")
location.send_keys(Keys.ENTER)

#click on jobs
jobs = driver.find_elements_by_css_selector(".job-card-container relative job-card-list job-card-container-\
-clickable job-card-list--underline-title-on-hover jobs-search-results-list__list-item--active jobs-\
search-two-pane__job-card-container--viewport-tracking-0")

for item in jobs:
    item.find_element_by_tag_name("a").click()
    driver.find_element_by_css_selector(".jobs-save-button artdeco-button \
    artdeco-button--3 artdeco-button--secondary").click()
    time.sleep(300)


