fo = open("test.txt", "r")
letter = []
taglist = []
for i in fo.readlines():
    if i != '\n':
        alist = i.strip().split('\t')
        if len(alist) == 1:
            word1 = ' '
            tag = alist[0]
        else:
            word1 = alist[0]
            tag = alist[1]
        letter.append(word1)
        taglist.append(tag)
fo.close()
f = open("dictionarycrfpre.txt", "r")
pretaglist = []
for a in f.readlines():
    if a != '\n':
        alist1 = a.strip().split(' ')
        if len(alist1) == 1:
            word2 = ' '
            tag1 = alist1[0]
        else:
            word2 = alist1[0]
            tag1 = alist1[1]
        pretaglist.append(tag1)
f.close()

pk = open('./dictionarycrfresult.txt', 'a', encoding='utf-8')
for e in range(len(letter)):
    target = letter[e] + ' ' + taglist[e] + ' ' + pretaglist[e]
    pk.write(target)
    pk.write('\n')