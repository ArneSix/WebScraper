from Requester import Requester
from Beautify import Beautify


class PageScraper:
    __page_content = None
    __requester = None
    __beautify = None

    def __init__(self, url):
        try:
            self.__requester = Requester(url)
            self.__beautify = Beautify(tag_name="div", class_name="jam", id_name="test")

        except KeyError as err:
            print(f"Wrong key delivered {err}")

    def initialize(self):
        self.__page_content = self.__requester.get_page_content()
        self.__beautify.load_content(self.__page_content)
        self.__beautify.find_data()


scraper = PageScraper('localhost:3000')
scraper.initialize()
