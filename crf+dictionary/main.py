from CRF import *

trainWordLists, trainTagLists = prepareData('./train.txt')
testWordLists, testTagLists = prepareData('./test.txt')
crf = CRFModel()
crf.train(trainWordLists, trainTagLists)
crf.test(testWordLists, testTagLists)
print('ok')
