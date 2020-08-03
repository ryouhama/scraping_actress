import os
import logging

import config

from file_manager import FileWriter
from request_manager import Scraper
from html_analyser import HtmlAnalyser


# set logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format=config.LOG_FORMAT)
# set Scraping page num
CNT_PAGE_NUM = 10
# set base url
BASE_URL = 'https://gensun.org/list_ja_female'
# set csv info
CSV_FILE_PATH = config.CSV_FILE_NAME
CSV_DIR = os.getcwd() + '/'


def main():
    """
    main
    """
    # create FileWriter Object
    fw = FileWriter(CSV_FILE_PATH)
    # write Header Info
    fw.write_header()
    # create Scraper
    scraper = Scraper()
    # create HTML Analyser
    analyser = HtmlAnalyser()
    url = ''
    cnt = 0

    for i in range(CNT_PAGE_NUM):
        # create url path
        if i == 0:
            url = BASE_URL + '.html'
        else:
            url = BASE_URL + '_' + str(i) + '.html'
        # scraping girls data
        response = scraper.scrape_actress_data(url)
        # get girls data
        actress_data_list = analyser.get_actress_list_from_response(response)
        # write csv to girls data
        cnt += fw.write_actress_data(actress_data_list)

    logger.info('取得データ数:' + str(cnt))


if __name__ == '__main__':
    main()
