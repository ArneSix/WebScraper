from bs4 import BeautifulSoup


class Beautify:
    __content = None
    __tag = None
    __class = None
    __id = None

    def __init__(self, **config):
        self.__tag = config['tag_name'] or None
        self.__class = config['class_name'] or None
        self.__id = config['id_name'] or None

    def load_content(self, content):
        self.__content = content

    def find_data(self):
        try:
            if not self.__content:
                raise TypeError

            html = BeautifulSoup(self.__content, 'html.parser')

            for index, tag in enumerate(html.select(f"{self.__tag}.{self.__class}")):
                print(html.find_all("div", class_="primary_info"))

        except TypeError as err:
            print(f"None value encountered")
