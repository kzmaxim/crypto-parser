from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options


def get_listing(crypto_name):
    ua = UserAgent()
    options = Options()
    options.add_argument(ua.random)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"https://www.coingecko.com/en/coins/{crypto_name.lower()}")

    time.sleep(5)

    try:
        listing_date = driver.find_element(By.XPATH,
                                           '//*[contains(text(), "Genesis Date")]/following-sibling::td').text.strip()
    except:
        listing_date = 'Дата листинга не найдена'

    driver.quit()

    return listing_date
