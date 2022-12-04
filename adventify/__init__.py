from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import pathlib, os

options = webdriver.ChromeOptions()
profile = pathlib.Path(os.getenv("HOME","/tmp")).joinpath('.config','chromium')

options.add_argument(r'user-data-dir={}'.format(profile))
options.add_argument("--headless")

def fetch_input(day=1) -> str:
    driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver-105"), options=options)
    driver.get(f'https://adventofcode.com/2022/day/{day}/input')
    driver.implicitly_wait(5)
    element = driver.find_element(By.XPATH, "/html/body")
    content = element.text
    if content.startswith("Please"):
        raise Exception("Unreleased content or something")
    else:
        with open("input","w") as outfile:
            outfile.write(content)
    driver.quit()
    return content
