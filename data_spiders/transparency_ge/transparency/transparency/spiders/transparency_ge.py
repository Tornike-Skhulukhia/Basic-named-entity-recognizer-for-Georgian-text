import requests
import scrapy

"""
Good resource for popular name & surnames to use in our extractor lists.

We can differentiate persons and companies from result by their id length - persons have 11 characters in them.
"""


class TransparencyGeSpider(scrapy.Spider):
    name = "transparency_ge"
    handle_httpstatus_list = [404]
    seen_parties = set()
    stop_spider = False

    def start_requests(self):
        self.max_parties_num = len(
            requests.get(
                "https://transparency.ge/politicaldonations/ge/party-names"
            ).json()
        )
        url = "https://transparency.ge/politicaldonations/ge/party/1/donor?year=all&sort=donationsum&direction=desc&page=all"

        yield scrapy.Request(url, callback=self.parse_results)

    def parse_results(self, response):
        if len(self.seen_parties) == self.max_parties_num:
            return

        party = response.css(".shemocirulebebi-head-name ::text").get()

        if party:
            self.seen_parties.add(party)

        # if successfull try next page
        curr_page_num = int(
            response.request.url.split("ge/politicaldonations/ge/party/")[1].split(
                "/donor?year"
            )[0]
        )

        yield scrapy.Request(
            response.request.url.replace(
                f"party/{curr_page_num}/donor", f"party/{curr_page_num + 1}/donor"
            ),
            callback=self.parse_results,
        )

        # get current page data

        headers = response.css(
            ".shemocirulobebi-inner-table thead tr a span::text"
        ).getall()

        headers = [*headers, "party"]

        for td in response.css(".shemocirulobebi-inner-table tbody > tr"):
            row_data = [i.strip() for i in td.css("td ::text").getall() if i.strip()]

            row_data.append(party)
            item = dict(zip(headers, row_data))

            yield item
