import os
import json
import requests
import io
import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


with io.open(sys.argv[1], 'r', encoding='utf-8')  as f:
    books = json.load(f)

for book in books:
    try:
        url = book['cover']
        filename = book['id'] + '-' + url.split('/')[-1]
        res = requests.get(url, headers=headers)
        with open(os.path.join(os.getcwd(), 'images', filename), 'wb') as W:
            W.write(res.content)

        book['cover'] = filename
    except:
        print('Error while download image for ' + book[id])
        continue

with io.open(sys.argv[1], 'w', encoding='utf-8') as outfile:
    outfile.write(unicode(json.dumps(books, ensure_ascii=False)))