from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.log import *
from scrapy_rakitan.settings import *
from scrapy_rakitan.items import *
#import pprint
from MySQLdb import escape_string
#import urlparse
import hashlib

cursor = CONN.cursor()  # important MySQLdb Cursor object 

def encode(str):
    return str.encode('utf8', 'ignore')


def encode_post(text):
    '''
    INPUT  : Raw Text (contains html is ok)
    OUTPUT : Fresh Text (MySQL Escaped and Stripped)
    '''
#    text = text.encode('ascii','ignore').strip()
    try :
        text = text.encode('ascii','replace')
    except:
        print '\nDECODE ERROR Encode Post\n' + text
    text = text.strip()
    text = re.sub('\t','',text)
    text = re.sub('\n','',text)
    text = re.sub('\r','',text)    
    try:
        text = MySQLdb.escape_string(text)
    except:
#        hash = hashlib.sha224(text).hexdigest()
        print '\nESCAPE ERROR ENCODE Post\n' + text
    return text


def insert_table(datas):
    sql = "INSERT INTO %s (Hash, item_name, item_price, item_link, item_category) \
values('%s', '%s', '%s', '%s', '%s')" % (SQL_TABLE,
    hashlib.sha224(datas['item_name']).hexdigest(),
    escape_string(datas['item_name']),
    escape_string(datas['item_price']),
    escape_string(datas['item_link']),
    escape_string(datas['item_category'])
    )
#    print sql
    if cursor.execute(sql):
        print "Inserted"
    else:
        print "Something wrong"

def complete_url(string):
    """Return complete url"""
    return "http://rakitan.com/" + string

class RakitanSpider(CrawlSpider):

    name = 'scrapy_rakitan_spider'
    start_urls = [
        'http://rakitan.com/'
    ]
    total = 0

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        # HXS to find url that goes to detail page
	c = 0
        items = hxs.select('//div/a/@href')
	title = items.select('/text()').extract()
        for item in items:
	    c += 1
            link = item.extract()
            #print complete_url(link)
	    #if (c == 1):
	    yield Request(complete_url(link), callback=self.parse_category)

	print "Total = " + `self.total`


    def parse_category(self, response):
	i = 0
        hxs = HtmlXPathSelector(response)
        # HXS to Detail link inside td and a
	category = hxs.select('//td[@align="CENTER"]/font/b/text()').extract()[0]
        items = hxs.select('//tr[@bgcolor="#DDDDDD" or @bgcolor="#FFFFFF"]')
        for item in items:
	    rakitan = ScrapyRakitanItem()
	    rakitan['item_name'] = item.select('td[1]/text()').extract()[0]
	    rakitan['item_price'] = item.select('td[2]/text()').extract()[0]
	    rakitan['item_link'] = unicode(response.url,'utf_8')
	    rakitan['item_category'] = category
#	    print rakitan
	    insert_table(rakitan)
	    self.total += 1
	    
	CONN.commit()
	return self.total
