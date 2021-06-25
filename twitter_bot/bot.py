from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# bot to complain about internet speed

PROMISED_DOWN = 150
PROMISED_UP = 10

CHROME_DRIVER_PATH = "C:\selenium_drivers\chromedriver.exe"

TWITTER_EMAIL = 'yourtwitteremail'
TWITTER_PW = "yourtwitterpassword"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element_by_class_name("start-text").click()
        time.sleep(50)
        self.down = self.driver.find_element_by_class_name("download-speed").text
        self.up = self.driver.find_element_by_class_name("upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        self.driver.find_element_by_css_selector('[href^="/login"]').click()
        time.sleep(1)
        self.driver.find_element_by_name("session[username_or_email]").send_keys(TWITTER_EMAIL)
        password_entry = self.driver.find_element_by_name("session[password]")
        password_entry.send_keys(TWITTER_PW)
        password_entry.send_keys(Keys.ENTER)
        if complain_bot.up < PROMISED_UP or complain_bot.down < PROMISED_DOWN:
            self.driver.find_element_by_class_name("public-DraftEditor-content")\
                .send_keys(f"@yourISPprovider Hello, my internet upload speed is " \
                    f"currently {self.up} and download speed is {self.down} this is not " \
                    f"fully meeting the promised upload speed of {PROMISED_UP} and download speed of {PROMISED_DOWN}")
            self.driver.find_element_by_xpath("//span[text()='Tweet']").click()


complain_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

complain_bot.get_internet_speed()

print(complain_bot.up)
print(complain_bot.down)

complain_bot.tweet_at_provider()
