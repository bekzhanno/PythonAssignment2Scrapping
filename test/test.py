from src import *

class CryptoScrapper:
    def crypt(z):
        gckdriver = webdriver.Firefox()
        gckdriver.get(url)
        page = gckdriver.page_source
        page_soup = BeautifulSoup(page, 'html.parser')
        h = page_soup.findAll("h3", {"class": "sc-1q9q90x-0", "class": "gEZmSc"})
        rslt = page_soup.findAll("section", "wrapper")
        
        print(rslt[0].text)
