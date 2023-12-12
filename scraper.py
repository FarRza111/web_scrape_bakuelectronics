import requests
import abc
from _common import *
from dataclasses import dataclass
from abc import ABC, abstractmethod

class MyABC(ABC):

    @abstractmethod
    def get_soup(self):
        pass

    @abstractmethod
    def process_soup(self):
        pass

    def scrape(self):
        pass



class Scraper(MyABC):

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get_soup(self):
        req = fetch_page(self._url, self._headers)
        if req.status_code == 200:
            return form_soup(req, "html.parser")
        return None

    def process_soup(self, soup):
        records = defaultdict(list)

        for i in range(5):
            base_url = f"https://www.bakuelectronics.az/catalog/noutbuklar-komputerler/noutbuklar/?page="
            current_url = base_url + str(i)
            page = fetch_page(current_url, headers)
            fsoup = form_soup(page, "html.parser")
            results = fsoup.find_all('div', class_='product__value')
            titles = fsoup.find_all('a', class_='product__title')

            for result in results:
                price = result.find('span').text
                if price == "Qiymət":
                    price_div = result.find('div', class_='product__price--cur')
                    if price_div:
                        price = price_div.text
                records["Price"].append(price)
            records['Model'].extend([title.text for title in titles])

        data = pd.DataFrame(records)
        return data


    def save_to_path(self):
        return self.process_soup().to_excel('_data.xlsx')

    def __str__(self):
        return f'{self._url}{self._headers}'

    def scrape(self):
        pass




if __name__ == "__main__":

    url = "https://www.bakuelectronics.az/catalog/noutbuklar-komputerler/noutbuklar/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    scraper_obj = Scraper(url = url, headers=headers)
    parsed_html = scraper_obj.get_soup()
    processed_soup = scraper_obj.process_soup(parsed_html)
    saved_data = processed_soup.to_excel('_data_.xlsx')
    print(processed_soup)
    # print(processed_soup)



