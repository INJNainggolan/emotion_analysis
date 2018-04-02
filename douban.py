import requests as re
from bs4 import BeautifulSoup
def doubanget(filename,page,type):
    url="https://movie.douban.com/subject/3578939/comments?start={0}&limit=20&sort=new_score&status=P&percent_type={1}".format(page,type)
    result=re.get(url=url)

    soup=BeautifulSoup(result.text,'html.parser')
    for j in range(20):
        with open(filename, 'a',encoding='utf-8') as file:
            try:
                file.write(soup.select('.comment-item')[j].p.text)
            except:
                continue
def get_train_data():
    for i in range(10):
        doubanget('posdouban.txt',i*20,'h')
        doubanget('negdouban.txt',i*20,'l')

def get_test_data():
    for i in range(10):
        doubanget('pos_test.txt',i*20,'h')
        doubanget('neg_test.txt',i*20,'l')


