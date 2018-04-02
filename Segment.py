import jieba

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def sent2word(sentence):
    seglist=jieba.cut(sentence.strip())
    stopwords=stopwordslist('stopwords.txt')
    outstr=''
    for word in seglist:
        if word not  in stopwords:
            if word!='\t':
                outstr += word
                outstr += ' '
    return outstr
def seg(filein,fileout):


    inputs=open(filein,'r',encoding='utf-8')

    outputs=open(fileout,'w',encoding='utf-8')

    for line in inputs:
        line=sent2word(line)
        outputs.write(line+'\n')



    outputs.close()
    inputs.close()

seg('posdouban.txt','posout.txt')
seg('negdouban.txt','negout.txt')
seg('pos_test.txt','pos_test_cut.txt')
seg('neg_test.txt','neg_test_cut.txt')