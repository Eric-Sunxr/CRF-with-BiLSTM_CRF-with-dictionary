import random
import pickle
from sklearn.model_selection import RepeatedKFold
def read_corpus(corpus_path):
    """
    read corpus and return the list of samples
    :param corpus_path:
    :return: data
    """
    data = []#data里存放的是一段一段的文字
    with open(corpus_path,'r', encoding='utf-8') as fr:
        lines = fr.readlines()
    sent_, tag_ = [], []
    for line in lines:
        if line != '\n':
            # print(line)
            if len(line.strip().split())==1:
                char=' '
                label=line.strip().split()[0]
            else:
                [char, label] = line.strip().split()
            sent_.append(char)
            tag_.append(label)
        else:
            data.append((sent_, tag_))
            sent_, tag_ = [], []

    return data

def vocab_build(vocab_path, corpus_path, min_count):
    """

    :param vocab_path:
    :param corpus_path:
    :param min_count:
    :return:
    """
    data = read_corpus(corpus_path)
    word2id = {}
    for sent_, tag_ in data:
        for word in sent_:
            if word.isdigit():
                word = '<NUM>'
            elif ('\u0041' <= word <='\u005a') or ('\u0061' <= word <='\u007a'):
                word = '<ENG>'
            if word not in word2id:
                word2id[word] = [len(word2id)+1, 1]
            else:
                word2id[word][1] += 1
    low_freq_words = []
    for word, [word_id, word_freq] in word2id.items():
        if word_freq < min_count and word != '<NUM>' and word != '<ENG>':
            low_freq_words.append(word)
    for word in low_freq_words:
        del word2id[word]

    new_id = 1
    for word in word2id.keys():
        word2id[word] = new_id
        new_id += 1
    word2id['<UNK>'] = new_id
    word2id['<PAD>'] = 0

    print(len(word2id))
    with open(vocab_path, 'wb') as fw:
        pickle.dump(word2id, fw)

datas=read_corpus('train.txt')
kf = RepeatedKFold(n_splits=5, n_repeats=1, random_state=0)
cnt = 0
for train_index, test_index in kf.split(datas):
    print(len(train_index)+len(test_index))
    print(len(train_index))
    print(len(test_index))
    print('正在生成第{}份数据'.format(cnt))
    # print('train_index', train_index, 'test_index', test_index)
    for i in train_index:
        with open('train_data{}'.format(cnt), 'a', encoding='utf8') as f:
            # for i in range(len(train_index)):
            word, tag = datas[i]
            # print([word, tag])
            for k in range(len(word)):
                # print([word[j],tag[j]])
                f.writelines(str(word[k]) + '\t' + tag[k] + '\n')
            f.writelines('\n')
    for j in test_index:
        with open('test_data{}'.format(cnt), 'a', encoding='utf8') as f:
            # for j in range(len(test_index)):
            word, tag = datas[j]
            # print([word, tag])
            for m in range(len(word)):
                # print([word[j],tag[j]])
                f.writelines(str(word[m]) + '\t' + tag[m] + '\n')
            f.writelines('\n')
    cnt += 1



# # print(datas[0])
# random.shuffle(datas)
# print(len(datas))
# print(datas[0])
# a = 800
# train=datas[:a]
# print(len(train))
# # dev=datas[a:b]
# # print(len(dev))
# test=datas[a:]
# print(len(test))
# with open('train_data','w',encoding='utf8') as f:
#     for i in range(len(train)):
#         word,tag=train[i]
#         print([word,tag])
#         for j in range(len(word)):
#             # print([word[j],tag[j]])
#             f.writelines(str(word[j])+'\t'+tag[j]+'\n')
#         f.writelines('\n')
# with open('test_data','w',encoding='utf8') as f:
#     for i in range(len(test)):
#         word,tag=test[i]
#         print([word,tag])
#         for j in range(len(word)):
#             # print([word[j],tag[j]])
#             f.writelines(str(word[j])+'\t'+tag[j]+'\n')
#         f.writelines('\n')
# with open('dev_data','w',encoding='utf8') as f:
#     for i in range(len(dev)):
#         word,tag=dev[i]
#         print([word,tag])
#         for j in range(len(word)):
#             # print([word[j],tag[j]])
#             f.writelines(str(word[j])+'\t'+tag[j]+'\n')
#         f.writelines('\n')
# print(datas[0])
# vocab_build('word2id.pkl','train.txt',0)