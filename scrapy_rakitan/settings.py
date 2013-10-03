# Scrapy settings for scrapy_rakitan project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_rakitan'

SPIDER_MODULES = ['scrapy_rakitan.spiders']
NEWSPIDER_MODULE = 'scrapy_rakitan.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_rakitan (+http://www.yourdomain.com)'


import sys
import MySQLdb

# SQL DATABASE SETTING
SQL_DB = 'scrapy_rakitan'
SQL_TABLE = 'rakitan'
SQL_HOST = 'localhost'
SQL_USER = 'root'
SQL_PASSWD = 'sukasepjay'

# connect to the MySQL server
try:
    CONN = MySQLdb.connect(host=SQL_HOST,
                         user=SQL_USER,
                         passwd=SQL_PASSWD,
                         db=SQL_DB)
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

