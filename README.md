## What to install
You need to have scrapy installed
```
conda install -c conda-forge scrapy
```
For more instructions on installation of scrapy,
https://docs.scrapy.org/en/latest/intro/install.html

Your also need to have python 3.8 installed.
## How to test
First install scrapy, then create a text file containing a personality on every line.
if the text file is named "names.txt",
```
python predict_type.py --testcase 5 --inputfile “names.txt”
```
I assume you have python and scrapy installed.
## What to do
To run this on a text file,
```
python predict_type.py --testcase 5 --inputfile “names.txt”
```
## What does this thing use
It makes crawlers crawl google search page for some personalities and get lots of text to do sentiment analysis.
To do this, I have used the python library (package in the python terminology) scrapy. (check the spiders/quotes_spider.py and predict_type.py)

## I am lazy, I like web
https://personality-check-99.herokuapp.com/
