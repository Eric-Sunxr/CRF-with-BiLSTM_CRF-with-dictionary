from sklearn.metrics import classification_report,confusion_matrix,precision_score,recall_score,precision_recall_curve,f1_score
from seqeval.metrics import classification_report as cr

import matplotlib.pyplot as plt
import matplotlib as mpl

def read_result(result_path):
    label=[]
    pred=[]
    with open(result_path,encoding='utf8') as f:
        for line in f.readlines():
            if line=='\n':
                continue
            else:
                text=line.strip().split(' ')
                label.append(text[-2])
                pred.append(text[-1])
    return label,pred

label,pred=read_result('crfresult1.txt')
# print(classification_report(label,pred))
# print(cr(label,pred,digits=6))
print(confusion_matrix(label,pred))
print("precision:")
print(precision_score(label,pred,average='macro'))
print("recall:")
print(recall_score(label,pred,average='macro'))
print("f1-score:")
print(f1_score(label,pred,average='macro'))

# # 支持中文字体显示, 使用于Mac系统
# # zhfont=mpl.font_manager.FontProperties(fname="/Library/Fonts/Songti.ttc")
#
# classes = ['0','body-B','body-I','disease-B','disease-I','medicine-B','medicine-I','operation-B','operation-I']
# confusion = confusion_matrix(label, pred)
#
# # 绘制热度图
# plt.imshow(confusion, cmap=plt.cm.Greens)
# indices = range(len(confusion))
# plt.xticks(indices, classes)
# plt.yticks(indices, classes)
# plt.colorbar()
# plt.xlabel('y_pred')
# plt.ylabel('y_true')
#
# # 显示数据
# for first_index in range(len(confusion)):
#     for second_index in range(len(confusion[first_index])):
#         plt.text(first_index, second_index, confusion[first_index][second_index])
#
# # 显示图片
# plt.show()