import requests


class Scraper:
    def __init__(self):
        """
        initial object
        """
        self.HTTP_ACCESS_OK = 200
        self.BASE_URL = 'https://gensun.org/list_ja_female'

    def scrape_actress_data(self, url):
        """
        scraping actress data and return response
        """
        ret_data = None

        response = requests.get(url)

        if self.HTTP_ACCESS_OK == response.status_code:
            ret_data = response
        return ret_data
