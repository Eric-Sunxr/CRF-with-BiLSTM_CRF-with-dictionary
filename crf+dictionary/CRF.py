# encoding = 'utf-8'
from sklearn_crfsuite import CRF
from seqeval.metrics import classification_report
from util import *

class CRFModel(object):
    def __init__(self,
                algorithm = 'lbfgs',
                c1 = 0.3,
                c2 = 0.2,
                max_iterations = 100):
        self.model = CRF(algorithm=algorithm,
                         c1=c1,
                         c2=c2,
                         max_iterations=max_iterations)

    def train(self, sentences, tag_lists):
        feature = [sent2feature(s) for s in sentences]
        self.model.fit(feature, tag_lists)

    def test(self, testWordLists, testTagLists):
        feature = [sent2feature(s) for s in testWordLists]
        tagPres = self.model.predict(feature)
        f = open('./crf.txt', 'a', encoding='utf-8')
        for i in range(len(testWordLists)):
            for j in range(len(testWordLists[i])):
                target = testWordLists[i][j] + ' ' + tagPres[i][j]
                f.write(target)
                f.write('\n')
            f.write('\n')
        print(classification_report(testTagLists, tagPres, digits=6))