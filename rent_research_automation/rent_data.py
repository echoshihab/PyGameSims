from bs4 import BeautifulSoup
from selenium import webdriver
import time


class RENT_DATA:
    def __init__(self, sel_driver_path):
        self.price_list = []
        self.address_list = []
        self.url_list = []
        self.driver = webdriver.Chrome(sel_driver_path)

    def scrape_rent_data(self, site_to_scrape):
        soup = BeautifulSoup(site_to_scrape.text, 'html.parser')
        items = soup.select('.list-card-info')

        # loop through all items if more data is desired
        for i in range(1, 5):
            self.price_list.append(items[i].select_one('.list-card-price').getText())
            self.address_list.append(items[i].select_one('.list-card-addr').getText())
            self.url_list.append(items[i].select_one('a')['href'])

    def submit_forms(self, forms_site):
        self.driver.get(forms_site)
        for i in range(len(self.price_list)):
            time.sleep(2)
            form = self.driver.find_element_by_class_name("freebirdFormviewerViewItemList")
            button = self.driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel")
            inputs = form.find_elements_by_tag_name('input')
            self.__submit_data(input_elements=inputs, button_element=button, data_index=i)
            time.sleep(1)
            self.__confirm_submission()

    def __submit_data(self, input_elements, button_element, data_index):
            input_elements[0].send_keys(self.address_list[data_index])
            input_elements[1].send_keys(self.price_list[data_index])
            input_elements[2].send_keys(self.url_list[data_index])
            button_element.click()

    def __confirm_submission(self):
        confirm_submission = self.driver.find_element_by_class_name("freebirdFormviewerViewResponseLinksContainer")
        link = confirm_submission.find_element_by_tag_name('a')
        link.click()
        time.sleep(2)
