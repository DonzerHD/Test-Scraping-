import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import BookItem  # Remplacez 'myproject' par le nom de votre projet

class BooksCrawlSpider(CrawlSpider):
    name = "books_crawl"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow=r"catalogue/"), callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        books = response.css(".product_pod")
        for book in books:
            title = book.css("h3 a::attr(title)").get()
            url = book.css("h3 a::attr(href)").get()
            book_url = response.urljoin(url)
            yield scrapy.Request(book_url, callback=self.parse_book, meta={'title': title})

    def parse_book(self, response):
        title = response.meta['title']
        description = response.css("#product_description+ p::text").get()

        book_item = BookItem()
        book_item["title"] = title
        book_item["description"] = description

        yield book_item