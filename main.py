from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from listing import get_listing
import pandas as pd
import random

ua = UserAgent()
options = Options()
options.binary_location = '/usr/bin/google-chrome'
options.add_argument(ua.random)
proxies = [
    '219.140.149.208:8090',
    '223.205.185.248:8080',
    '222.70.20.234:5678',
    '221.10.57.128:5138',
    '147.45.48.237:8080',
]

proxy = random.choice(proxies)
options.add_argument(f'--proxy-server={proxy}')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://ru.tradingview.com/crypto-coins-screener/")
time.sleep(5)

crypto_rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
crypto_data = []

for row in crypto_rows:
    name = row.find_element(By.CSS_SELECTOR, 'td sup').text.strip()
    price = row.find_element(By.CSS_SELECTOR, 'td:nth-of-type(3)').text.strip()
    listing = get_listing(name)

    crypto_data.append([name, listing, price])

driver.quit()
df = pd.DataFrame(crypto_data, columns=['Название криптовалюты', 'Дата листинга', 'Цена'])
df.to_excel('crypto_data.xlsx', index=False)

print("Данные сохранены в 'crypto_data.xlsx'")


