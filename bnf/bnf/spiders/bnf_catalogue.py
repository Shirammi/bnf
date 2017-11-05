from scrapy import Spider
from scrapy import Selector
import bnf.items
import datetime


class GareSpider(Spider):
    name = "gare"
    allowed_domains = ["catalogue.bnf.fr"]
    start_urls = [
        "http://catalogue.bnf.fr/resultats-sujet.do?sujet=Gares&filtre=1&pageRech=rsu",
    ]

    def parse(self, response):
        titres = Selector(response).xpath('//div[@class="notice-libelle"]')

        for titre in titres:
            item = bnf.items.BnfItem()
            item['titre'] = titre.xpath('a/text()')
            item['url'] = titre.xpath('a/@href')
            item['temps_du_scrap'] = datetime.datetime()

            return item


