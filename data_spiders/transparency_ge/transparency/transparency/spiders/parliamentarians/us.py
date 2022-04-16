from ast import Assert
import requests
import scrapy
from urllib.parse import unquote

# def _rm_brackets_from_name_surname(name_surname):
#     name_surname = name_surname.strip()

#     if name_surname.endswith(')'):
#         name_surname = name_surname.rsplit("(", maxsplit=1)[0].strip()

#     try:
#         assert " " in name_surname

#         # word must not be only digits
#         assert all([not i.isdigit() for i in name_surname.split()])

#     except AssertionError:
#         return ""

#     return name_surname


class UsSpider(scrapy.Spider):
    name = "parliamentarians_us"
    start_urls = ["https://www.dems.gov/who-we-are/our-members"]

    def parse(self, response):
        for i in response.css('#member-list div.front img'):

            yield {
                "name_surname": i.css('::attr(alt)').get(),
                "image_url": response.urljoin(i.css('::attr(src)').get())
            }

