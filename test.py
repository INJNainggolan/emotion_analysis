
from bs4 import BeautifulSoup
import requests

with requests.session() as s:
    url = 'https://club.jd.com/comment/productPageComments.action'
    data = {
        'productId':'3888284',
        'score':0,
        'sortType':5,
        'pageSize':10,
        'isShadowSku':0,
        'page':0
    }
    r = s.get(url, params = data)
    print(r.json())



