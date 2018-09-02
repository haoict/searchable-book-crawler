import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
from pymongo import MongoClient
import io


with io.open('./json/' + sys.argv[1], 'r', encoding='utf-8') as f:
    books = json.load(f)

client = MongoClient('mongodb://root:admin123@haoict.com:27017/rrchat?authSource=admin')

db = client.mdstbooks
books_collection = db.books

x = books_collection.insert_many(books)
print(x.inserted_ids)
