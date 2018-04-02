import logging
from  gensim.models  import word2vec
from gensim.models.word2vec import  Word2Vec
logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)
sentcens=word2vec.Text8Corpus('allpos.txt')
model = Word2Vec(sentcens,size=40)
model.save('save.model')