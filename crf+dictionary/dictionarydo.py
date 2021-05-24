p = open("vocab.txt", "r")
words = []
label = []
for i in p.readlines():
    if i != '\n':
        alist = i.strip().split(' ')
        if len(alist) == 1:
            word = ' '
            tag = alist[0]
            words.append(word)
            label.append(tag)
        elif alist[0] == '，' or alist[0] == '、':
            continue
        else:
            word = alist[0]
            tag = alist[1]
            words.append(word)
            label.append(tag)
p.close()
fo = open("crf.txt", "r")
letter = []
taglist = []
for i in fo.readlines():
    if i != '\n':
        alist = i.strip().split(' ')
        if len(alist) == 1:
            word1 = ' '
            tag = alist[0]
        else:
            word1 = alist[0]
            tag = alist[1]
        letter.append(word1)
        taglist.append(tag)
fo.close()
# print(words)
# print(len(words[0]))
length = 0
for word in words:
    if len(word) > length:
        length = len(word)

z = 0
i = 0
while i < len(letter):
    yuan = ''
    signal = 0
    if i > 83625:
        z += 1
        for m in range(length-z):
            yuan += letter[i + m]
            for j in range(len(words)):
                if yuan == words[j]:
                    if label[j] == u'疾病和诊断':
                        if yuan == 1:
                            taglist[i] = 'B-DISEASE'
                        else:
                            taglist[i] = 'B-DISEASE'
                            for n in range(m):
                                taglist[i + n + 1] = 'I-DISEASE'
                            signal = m
                    # elif label[j] == u'解剖部位':
                    #     if yuan == 1:
                    #         taglist[i] = 'B-BODY'
                    #     else:
                    #         taglist[i] = 'B-BODY'
                    #         for n in range(m):
                    #             taglist[i + n + 1] = 'I-BODY'
                    #         signal = m
                    # elif label[j] == u'实验室检验':
                    #     if yuan == 1:
                    #         taglist[i] = 'B-LAB'
                    #     else:
                    #         taglist[i] = 'B-LAB'
                    #         for n in range(m):
                    #             taglist[i + n + 1] = 'I-LAB'
                    #         signal = m
                    elif label[j] == u'药物':
                        if yuan == 1:
                            taglist[i] = 'B-MEDICINE'
                        else:
                            taglist[i] = 'B-MEDICINE'
                            for n in range(m):
                                taglist[i + n + 1] = 'I-MEDICINE'
                            signal = m
                    elif label[j] == u'手术':
                        if yuan == 1:
                            taglist[i] = 'B-OPERATION'
                        else:
                            taglist[i] = 'B-OPERATION'
                            for n in range(m):
                                taglist[i + n + 1] = 'I-OPERATION'
                            signal = m
                    elif label[j] == u'影像检查':
                        if yuan == 1:
                            taglist[i] = 'B-PIC'
                        else:
                            taglist[i] = 'B-PIC'
                            for n in range(m):
                                taglist[i + n + 1] = 'I-PIC'
                            signal = m

    else:
        for m in range(length):
            yuan += letter[i + m]
            for j in range(len(words)):
                if yuan == words[j]:
                    if label[j] == u'疾病和诊断':
                        if yuan == 1:
                            taglist[i] = 'B-DISEASE'
                        else:
                            taglist[i] = 'B-DISEASE'
                            for n in range(m):
                                taglist[i + n + 1] = 'I-DISEASE'
                            signal = m
                    # elif label[j] == u'解剖部位':
                    #     if yuan == 1:
                    #         taglist[i] = 'B-BODY'
                    #     else:
                    #         taglist[i] = 'B-BODY'
                    #         for n in range(m):
                    #             taglist[i + n + 1] = 'I-BODY'
                    #         signal = m
                    # elif label[j] == u'实验室检验':
                    #     if yuan == 1:
                    #         taglist[i] = 'B-LAB'
                    #     else:
                    #         taglist[i] = 'B-LAB'
                    #         for n in range(m):
                    #             taglist[i + n + 1] = 'I-LAB'
                    #         signal = m
                    elif label[j] == u'药物':
                        if yuan == 1:
                            taglist[i] = 'B-MEDICINE'
                        else:
                            taglist[i] = 'B-MEDICINE'
                            for n in range(m):
                                taglist[i + n + 1] = 'I-MEDICINE'
                            signal = m
                    elif label[j] == u'手术':
                        if yuan == 1:
                            taglist[i] = 'B-OPERATION'
                        else:
                            taglist[i] = 'B-OPERATION'
                            for n in range(m):
                                taglist[i + n + 1] = 'I-OPERATION'
                            signal = m
                    elif label[j] == u'影像检查':
                        if yuan == 1:
                            taglist[i] = 'B-PIC'
                        else:
                            taglist[i] = 'B-PIC'
                            for n in range(m):
                                taglist[i + n + 1] = 'I-PIC'
                            signal = m
    i += signal + 1
f = open('./dictionarycrfpre.txt', 'a', encoding='utf-8')
for e in range(len(letter)):
    target = letter[e] + ' ' + taglist[e]
    f.write(target)
    f.write('\n')
