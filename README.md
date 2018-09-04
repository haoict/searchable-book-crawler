start crawl by scrapy:
$ cd scrapy_book
$ scrapy crawl timsach -o ../json/booksfull.json

download book cover image
$ python downloadimage.py ./json/books500.json

get ebook download link
$ python downloadebook.py ./json/books500.json

migrate to mongodb
$ python json2mongo.py ./json/books500.json