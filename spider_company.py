import os
import scrapy

HOST = os.environ.get('COMPANY_HOST')


class CompanySpider(scrapy.Spider):
    '''Spider for loading company catalog'''
    name = 'company'
    start_urls = [HOST + '/catalog/list.php?COMPANIES=1']

    def parse(self, response):
        '''Parse company list'''

        for title in response.css('div#container table.block td p a'):
            href = title.css('a::attr(href)')
            if href.re(r"detail"):
                company_page = HOST + href.extract_first()
                yield response.follow(company_page, self.parse_company)

        for next_page in response.xpath("//*[contains(text(), 'След.')]"):
            next_page = HOST + next_page.css('a::attr(href)').extract_first()
            yield response.follow(next_page, self.parse)
            break

    def parse_company(self, response):
        '''Parse company page details'''

        company_name = response.css('div#container table.block h1 ::text').extract_first()
        data = {
            'company_name': company_name,
        }
        for td in response.css('div#comblok_info table tr'):
            attr_name = td.css('td ::text').extract_first()
            attr_value = td.css('td:last-child ::text').extract_first()
            data[attr_name] = attr_value
        yield data
