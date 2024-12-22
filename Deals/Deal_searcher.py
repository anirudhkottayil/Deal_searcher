from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "profile.managed_default_content_settings.javascript": 2  # Disable JavaScript
})

class Deal_searcher(webdriver.Chrome):
    def __init__(self, teardown=False):
        super(Deal_searcher, self).__init__(options=chrome_options)
        self.implicitly_wait(10)
        self.maximize_window()

    def load_first_page(self, site_url):
        self.get(site_url)
        checkbox = self.find_element(By.NAME, "noexpired")
        if not checkbox.is_selected():
            checkbox.click()