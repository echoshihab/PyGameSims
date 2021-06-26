from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#this is a bot to target programmermemes__ instagram account and follow the followers


CHROME_DRIVER_PATH = "C:\selenium_drivers\chromedriver.exe"
TARGET_ACCOUNT = "programmermemes__"
USERNAME ="yourusername"
PASSWORD = "yourpassword"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        self.driver.find_element_by_name("username").send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.find_element_by_css_selector("input[placeholder='Search']").send_keys('programmermemes__')
        time.sleep(2)
        self.driver.find_element_by_css_selector("a[href='/programmermemes__/']").click()
        time.sleep(2)
        self.driver.find_element_by_css_selector("a[href='/programmermemes__/followers/']").click()
        time.sleep(2)

        #set this next block to loop if desired till last follower is reached
        #you can do this by looping till scrollTop value does not change
        element = self.driver.find_element_by_css_selector("div[class='isgrP']")
        time.sleep(1)
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].scrollHeight;',
                                   element)
        time.sleep(2)
        follow_buttons = element.find_elements_by_tag_name("button")
        self.follow(follow_buttons)

    def follow(self, elements):
        for item in elements:
            item.click()
            time.sleep(1)


instagramFollower = InstaFollower()

instagramFollower.login()
instagramFollower.find_followers()
