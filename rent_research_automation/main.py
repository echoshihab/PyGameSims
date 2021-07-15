from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

zillow_link = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.50279426574707%2C%22east%22%3A-122.35688209533691%2C%22south%22%3A37.753140425735936%2C%22north%22%3A37.83751326485209%7D%2C%22mapZoom%22%3A13%2C%22isMapVisible%22%3Atrue%2C%22category%22%3A%22cat2%22%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A926489%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Accept-Language": "en-US"
}

google_forms = 'https://docs.google.com/forms/d/e/1FAIpQLScBbgR0I6HFmat7U3oGpxpfvuyy1SpzYeY9M13k68a7XLCosA/viewform?usp=sf_link'

CHROME_DRIVER_PATH = "C:\selenium_drivers\chromedriver.exe"

#get listings info
rent_query_response = requests.get(url=zillow_link, headers=headers)

soup = BeautifulSoup(rent_query_response.text, 'html.parser')

items = soup.select('.list-card-info')

price_list = []
address_list = []
url_list = []

for i in range(1,5):
    price_list.append(items[i].select_one('.list-card-price').getText())
    address_list.append(items[i].select_one('.list-card-addr').getText())
    url_list.append(items[i].select_one('a')['href'])


# fill out google forms

driver = webdriver.Chrome(CHROME_DRIVER_PATH)

driver.get(google_forms)



print(price_list)

for i in range(len(price_list)):
    time.sleep(2)
    form = driver.find_element_by_class_name("freebirdFormviewerViewItemList")
    button = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
    inputs = form.find_elements_by_tag_name('input')
    inputs[0].send_keys(address_list[i])
    inputs[1].send_keys(price_list[i])
    inputs[2].send_keys(url_list[i])
    button.click()
    time.sleep(1)
    confirm_submission = driver.find_element_by_class_name("freebirdFormviewerViewResponseLinksContainer")
    link = confirm_submission.find_element_by_tag_name('a')
    link.click()
    time.sleep(2)
