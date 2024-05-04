from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent

import json

def create_driver():
    ua = UserAgent()
    random_ua = ua.random

    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={random_ua}")

    driver = webdriver.Chrome(options=chrome_options)

    return driver

def read_settings(SETTINGS_PATH):
    with open(SETTINGS_PATH, "r") as settings:
        data = json.load(settings)
    return data
