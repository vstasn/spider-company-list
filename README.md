# Spider-company

Scrapy-parser to load company catalog

## Requirements
* Python 3.6

## How to
1. Install requirements
```
pip install -r requirements.txt
```
2. Set environment variables
```
COMPANY_HOST=https://google.com
```
3. Set scrapy proxy
```
https_proxy=https://{PROXY_HOST}:{PROXY_PORT}
```
4. Start parser
```
scrapy runspider spider_company.py -o {filename.csv}
```