import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
from pymongo import MongoClient
import io
import no_accecnt_vietnamese_regex
from pprint import pprint

with io.open(sys.argv[1], 'r', encoding='utf-8') as f:
    books = json.load(f)

for book in books:
    name = book['name']
    book['normalized_name'] = no_accecnt_vietnamese_regex.no_accent_vietnamese(name.lower())

client = MongoClient('mongodb://admin:admin321@haoict.com:27017/mdstbooks?authSource=admin')

db = client.mdstbooks
books_collection = db.books

x = books_collection.insert_many(books)
print(x.inserted_ids)
