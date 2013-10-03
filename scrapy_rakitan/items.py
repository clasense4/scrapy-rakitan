# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ScrapyRakitanItem(Item):
    # define the fields for your item here like:
    # name = Field()

    item_link = Field()
    item_name = Field()
    item_category = Field()
    item_price = Field()
