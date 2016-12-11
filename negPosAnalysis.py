#!/usr/bin/python

def get_words(url):
    import requests
    words = requests.get(url).content.decode('latin-1')
    word_list = words.split('\n')
    index = 0
    while index < len(word_list):
        word = word_list[index]
        if ';' in word or not word:
            word_list.pop(index)
        else:
            index+=1
    return word_list

#Get lists of positive and negative words

def remove_punctuation(word):
    if word and ((word[-1] >= 'a' and word[-1]<='z') or (word[-1] >= 'A' and word[-1]<='Z')):
        return word
    elif word:
        return word[:-1]
    else:
        return word


def negPosAnalysis():
    p_url = 'http://ptrckprry.com/course/ssd/data/positive-words.txt'
    n_url = 'http://ptrckprry.com/course/ssd/data/negative-words.txt'
    positive_words = get_words(p_url)
    print(positive_words)
    negative_words = get_words(n_url)

    with open('InvestorForum.txt','r') as f:
        data = f.read()
        words = data.split()
        cpos=0
        cneg=0
        for word in words:
            word = remove_punctuation(word)
            if word in positive_words:
                cpos += 1
            if word in negative_words:
                cneg += 1
        total_words = len(words)
        ppct = cpos/total_words * 100
        npct = cneg/total_words * 100
        pos_neg_ratio = cpos/cneg
        with open("pos_neg_analysis.txt","a+") as f:
            f.write("total num of words: %7d"%len(words))
            f.write("ppct: %2.2f"%ppct)
            f.write("npct: %2.2f"%npct)
            f.write("pos_neg_ratio: %2.2f"%pos_neg_ratio)



