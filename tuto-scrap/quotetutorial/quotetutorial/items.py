# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data -> Temporary containers (items) -> Storing in database

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()

class BookItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    
class MovieItem(scrapy.Item):
    title = scrapy.Field()
    genre = scrapy.Field()