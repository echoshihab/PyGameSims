from selenium import webdriver



chrome_driver_path = "C:\selenium_drivers\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

#get price from amazon
# driver.get("https://www.amazon.ca/Infant-Optics-DXR-8-Monitor-Interchangeable/dp/B00ECHYTBI/\
# ref=sr_1_5?crid=2LUP11P6H9M73&dchild=1&keywords=infant+optics+dxr-8+pro+baby+monitor&qid=1620566812&sprefix=\n"
#            "nfant+Optics+DXR-8%2Caps%2C205&sr=8-5")
#
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

data_dict = {}
#get events from python docs
driver.get("https://www.python.org/")
events_list = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
events = events_list.find_elements_by_tag_name('li')

for index in range(len(events)):
    time = events[index].find_element_by_tag_name('time').get_attribute("datetime").split("T")[0]
    event_name = events[index].find_element_by_tag_name('a').text
    data_dict[index] = {
        "time": time,
        "name": event_name
    }

print(data_dict)
driver.quit()