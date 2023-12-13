import pandas as pd
import requests
from bs4 import BeautifulSoup
import typing as ty
from typing import Literal
from collections import defaultdict

url = "https://www.bakuelectronics.az/catalog/noutbuklar-komputerler/noutbuklar/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}


def fetch_page(
    url: str, headers: ty.Dict[str, ty.Any]
) -> ty.Union[requests.Response, str]:
    try:
        return requests.get(url=url, headers=headers)
    except requests.RequestException as e:
        return {"message": f"error occurred {e}"}


def form_soup(
    response: requests.Response, parser: Literal["html.parser", "lxml"] = "html.parser"
) -> BeautifulSoup:
    return BeautifulSoup(response.content, parser)


if __name__ == "__main__":
    records = defaultdict(list)

    for i in range(5):
        base_url = f"https://www.bakuelectronics.az/catalog/noutbuklar-komputerler/noutbuklar/?page="
        current_url = base_url + str(i)
        page = fetch_page(current_url, headers)
        fsoup = form_soup(page, "html.parser")

        results = fsoup.find_all("div", class_="product__value")
        titles = fsoup.find_all("a", class_="product__title")

        records["Model"].extend([title.text for title in titles])

        for result in results:
            price = result.find("span").text
            if price == "Qiymət":
                price_div = result.find("div", class_="product__price--cur")
                if price_div:
                    price = price_div.text
            records["Price"].append(price)

    data = pd.DataFrame(records)
    data.to_excel("mydata.xlsx")
    print(data)
