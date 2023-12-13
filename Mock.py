import requests
import unittest
from _common import fetch_page, form_soup
from unittest.mock import patch


class TestWebData(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.bakuelectronics.az"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }

    @patch("requests.get")
    def test_scrape_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "<html>returned content</html>"
        page = fetch_page(url=self.url, headers=self.headers)
        self.assertIsNotNone(page, "<html>returned content</html>")

    @patch("requests.get")  #
    def test_page_errors(self, mock_get):
        mock_get.side_effect = requests.RequestException("error occured")


if __name__ == "__main__":
    unittest.main()
