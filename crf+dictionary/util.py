def prepareData(filePath):
    f = open(filePath, 'r', encoding='utf-8', errors='ignore')
    wordlists, taglists = [], []
    wordlist, taglist = [], []
    for line in f.readlines():
        # print(line.strip())
        # print(line.strip().split(' '))
        if line =='\n':
            wordlists.append(wordlist); taglists.append(taglist)
            wordlist, taglist = [], []
        else:
            alist = line.strip().split('\t')
            if len(alist) == 1:
                word = ' '
                tag = alist[0]
            else:
                word = alist[0]
                tag = alist[1]
            wordlist.append(word); taglist.append(tag)
    if len(wordlist) != 0 or len(taglist) != 0:
        wordlists.append(wordlist); taglists.append(taglist)
    f.close()
    return wordlists, taglists

def word2feature(sent, i):
    word = sent[i]
    prev_word = '<s>' if i == 0 else sent[i-1]
    next_word = '</s>' if i == len(sent)-1 else sent[i+1]
    feature = {
        'w': word,
        'w-1': prev_word,
        'w+1': next_word,
        'w-1:w': prev_word+word,
        'w:w+1': word+next_word,
        'bias': 1
    }
    return feature

def sent2feature(sent):
    return [word2feature(sent, i) for i in range(len(sent))]