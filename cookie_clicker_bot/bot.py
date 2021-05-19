from selenium import webdriver
from datetime import datetime as dt, timedelta

chrome_driver_path = "C:\selenium_drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

store = driver.find_elements_by_css_selector("store")
current_time = dt.now()
time_delta_duration = timedelta(minutes=1)
time_delta_award = timedelta(seconds=5)


while dt.now() <= current_time + time_delta_duration:
    if dt.now() >= current_time+time_delta_award:
        time_delta_award += timedelta(seconds=5)
        can_buy_awards = driver.find_elements_by_css_selector('#store>div:not(.grayed)')
        award_cost_max = 0
        target_award = None
        #loop through active awards in store and click on item with most point
        for item in can_buy_awards:
            cost = int(item.find_element_by_tag_name('b').text.split('-')[1].strip())
            if cost > award_cost_max:
                award_cost_max = cost
                target_award = item
        if target_award is not None:
            target_award.click()
    driver.find_element_by_id("cookie").click()




