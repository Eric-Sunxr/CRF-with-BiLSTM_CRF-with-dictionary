from sklearn.model_selection import RepeatedKFold


def read_corpus(corpus_path):
    """
    read corpus and return the list of samples
    :param corpus_path:
    :return: data
    """
    data = []  # data里存放的是一段一段的文字
    with open(corpus_path, 'r', encoding='utf-8') as fr:
        lines = fr.readlines()
    sent_, tag_ = [], []
    for line in lines:
        if line != '\n':
            if len(line.strip().split()) == 1:
                char = ' '
                label = line.strip().split()[0]
            else:
                [char, label] = line.strip().split()
            sent_.append(char)
            tag_.append(label)
        else:
            data.append((sent_, tag_))
            sent_, tag_ = [], []

    return data


datas = read_corpus('train.txt')
kf = RepeatedKFold(n_splits=5, n_repeats=1, random_state=0)
cnt = 0
for train_index, test_index in kf.split(datas):
    print('正在生成第{}份数据'.format(cnt))
    for i in train_index:
        with open('train_data{}'.format(cnt), 'a', encoding='utf8') as f:
            word, tag = datas[i]
            for k in range(len(word)):
                f.writelines(str(word[k]) + '\t' + tag[k] + '\n')
            f.writelines('\n')
    for j in test_index:
        with open('test_data{}'.format(cnt), 'a', encoding='utf8') as f:
            word, tag = datas[j]
            for m in range(len(word)):
                f.writelines(str(word[m]) + '\t' + tag[m] + '\n')
            f.writelines('\n')
    cnt += 1
