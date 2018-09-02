import os
import json
import requests
import urllib2
import io

import sys
reload(sys)
sys.setdefaultencoding('utf8')

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

base_url = "http://timsach.top/download/"

epub = "epub"
mobi = "mobi"
pdf = "pdf"

sachvui = "/"
dtvebook = "_dvt/"
ebooks4pw = "_ebooks4pw/"
dls = "_dls/"
lt = "_lt/"

def get_link(i, type, source):
    try:
        url = base_url + type + source + str(i)
        response = urllib2.urlopen(url)
        page_source = response.read()
        matched_lines = [line for line in page_source.split('\n') if "location.href" in line][0]
        dlink = matched_lines.strip().replace('location.href = "', '').replace('";', '')
        #print dlink
        return dlink
    except urllib2.HTTPError, e:
        print str(e.code) + ' ' + url
        return ''

def get_link_by_type(i, type):
    link = ''
    link = get_link(i, type, sachvui)
    if link == '':
        link = get_link(i, type, dtvebook)
    if link == '':
        link = get_link(i, type, ebooks4pw)
    if link == '':
        link = get_link(i, type, dls)
    if link == '':
        link = get_link(i, type, lt)
    return link

with io.open(sys.argv[1], 'r', encoding='utf-8') as f:
    books = json.load(f)

for book in books:
    i = book['id']
    epub_link = get_link_by_type(i, epub)
    mobi_link = get_link_by_type(i, mobi)
    pdf_link = get_link_by_type(i, pdf)
    book['epub_link'] = epub_link
    book['mobi_link'] = mobi_link
    book['pdf_link'] = pdf_link
    #book = {"id": i, "epub_link": epub_link, "mobi_link": mobi_link, "pdf_link": pdf_link}
    #books.append(book)

with io.open(sys.argv[1], 'w', encoding='utf-8') as outfile:
    outfile.write(unicode(json.dumps(books, ensure_ascii=False)))