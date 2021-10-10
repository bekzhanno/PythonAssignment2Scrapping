from bs4 import BeautifulSoup
from selenium import webdriver

coin = input("crypto name: ")
url = f'https://coinmarketcap.com/currencies/{coin}/news/'
driver = webdriver.Firefox()

