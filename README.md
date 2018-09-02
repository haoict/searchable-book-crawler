start crawl by scrapy:
$ scrapy crawl timsach -o ../json/books50.json

download book cover image
$ python downloadimage.py ./json/books50.json

get ebook download link
$ python downloadebook.py ./json/books50.json

migrate to mongodb
$ python json2mongo.py ./json/books50.json