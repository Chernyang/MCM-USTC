import collections
import re
def stopwordslist():
    #delete stop words
    stopwords = [line.strip() for line in open('./stopwords.txt').readlines()]
    return stopwords

def count_word(filename):
    """count filename word frequency
    :param filename:
    """
    # return value is dict,will count automatically
    word_counter=collections.Counter()

    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            #Convert to lowercase
            line=line.lower()
            word_counter.update([word for word in re.split('\s+',line) if word !=''])
    return dict(word_counter)

def get_top(filename,topk=10):
    """
    :param filename:the file you want to count word frequency
    :param topk:you want to return the first topk words with the highest frequency
    """
    word_dict=count_word(filename)
    topk_words=sorted(word_dict.items(),key=lambda x:x[1],reverse=True)
    return topk_words[:topk]


if '__main__'==__name__:
    import sys
    stopwords = stopwordslist()
    fout=open('output.txt','w')
    if len(sys.argv)!=3:
        print('Usage: {} filename topk'.format(sys.argv[0]),file=sys.stderr)
        sys.exit(0)
    top_words=get_top(sys.argv[1],int(sys.argv[2]))
