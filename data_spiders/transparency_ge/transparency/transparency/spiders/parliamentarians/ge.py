import scrapy
from urllib.parse import unquote

def _rm_brackets_from_name_surname(name_surname):
    name_surname = name_surname.strip()

    if name_surname.endswith(')'):
        name_surname = name_surname.rsplit("(", maxsplit=1)[0].strip()

    try:
        assert " " in name_surname

        # word must not be only digits
        assert all([not i.isdigit() for i in name_surname.split()])

    except AssertionError:
        return ""

    return name_surname


class GeSpider(scrapy.Spider):
    name = "parliamentarians_ge"
    start_urls = ["https://ka.wikipedia.org/wiki/საქართველოს_პარლამენტი"]

    def parse(self, response):
        for i in response.css('table[cellspacing="0"] li a[href][title]'):

            yield {
                "name_surname": _rm_brackets_from_name_surname(
                    i.css('::attr(title)').get()
                ),
                "profile_url": unquote(
                    response.urljoin(i.css('::attr(href)').get())
                )
            }

