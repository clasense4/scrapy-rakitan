# Scrapy Rakitan

This Crawler is for crawl an online shop [Rakitan](http://www.rakitan.com).
It will save the item name, link, categories and price in MySQL.

## How to Use :
1. Clone this repository

        git clone https://github.com/clasense4/scrapy-rakitan.git

2. Edit `scrapy_rakitan/settings.py` change your `scrapy` and `MySQL` setting
3. Insert this SQL query :
        
        CREATE TABLE `rakitan` (
          `IID` int(11) NOT NULL AUTO_INCREMENT,
          `Hash` text NOT NULL,
          `Item_name` text NOT NULL,
          `Item_price` text NOT NULL,
          `Item_category` text NOT NULL,
          `Item_link` text NOT NULL,
          `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY (`IID`)
        ) ENGINE=InnoDB AUTO_INCREMENT=6642 DEFAULT CHARSET=latin1

4. Start your crawler with this command

        $> scrapy crawl scrapy_rakitan

9. At `04 October 2013 : 4.00 AM`, this script give me `6641 Items`.

## Notice
The script is still sucks, just for fun, not follow scrapy standards, use at your own risks.

mail me at clasense4[at]gmail[dot]com

[@clasense4](http://twitter.com/clasense4)
