#!/usr/bin/python

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import re
import string



#Remove short words
def remove_short_words(text_string,exclude):
    shortword=re.compile(r'%s '%exclude)
    return shortword.sub(' ',text_string)

#Remove punctuation
def removePunctuation(text_string):
    return text_string.translate(None, string.punctuation)
    #return re.sub(r'[^\w\s]','',text_string)

def processWord():
    #with open("InvestorForum.txt",'r') as f:
    a=["going","people","lendingclub","Lending","doesn","note","investor","rate","PM","LC","will","Lending","time","Quote","month","payment","see","will","good","change","people","one","Folio","cash","work","sure","value","bank","put","number","better","many","less","come","credit","lendingclub","loan","account","lendingclub","number","probably","getting","January","February","March","April","May","June","July","August","September","October","November","December","actually","pretty","maybe","Thank","listed","nothing","notes","still"]
    with open("processedWord.txt",'r') as f:
        text=f.read()
    for i in a:
        text=remove_short_words(text,a)
    with open("processedWord.txt",'w') as f:
        f.write(text)

if __name__ == "__main__":
    processWord()
