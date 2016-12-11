#!/usr/bin/python

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.probability import FreqDist
import re

def cloudWord():
    text=''
    with open("processedWord.txt",'r') as f:
        text=f.read()

    stopwords = STOPWORDS.copy()
    additional_stop_words={"quote","note","investor","rate","PM","LC","will","Lending","time","Quote","month","payment","see","will","good","change","people","one","Folio","cash","work","sure","value","bank","put","number","better","many","less","come","credit","lendingclub","loan","account","lendingclub","number","probably","getting","January","February","March","April","May","June","July","August","September","October","November","December","actually","pretty","maybe","Thank","listed","nothing","notes","still"}
    for i in additional_stop_words:
        stopwords.add(i)

    wordcloud = WordCloud(stopwords=STOPWORDS,background_color='white',width=1200,height=1000).generate(text)

    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    cloudWord()



