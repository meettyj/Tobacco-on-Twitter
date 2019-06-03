import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

def computeAccuracy(y_predict, y_gt):
# comps = y_test[:100] != pred_alc_new[:100]
    comps = y_gt != y_predict
    # print(comps[:100])
    print('length of total comps: ', len(comps))
    diff = list(np.where(comps)[0])
    # print('length of difference: ', len(diff))
    # print(diff)
    print('pretrained alcohol classifer:  %d different item in whole dataset'%(len(diff)))
    acc = (len(comps)-len(diff))/len(comps)*100
    print('accuracy: %f%%'%(acc))
    return acc


def computeF1Score(y_gt, y_predict):
#     kwargs = {}
#     kwargs["average"] = 'micro'
#     f1 = f1_score(y_true=y_gt, y_pred=y_alc_initial, **kwargs)
    f1 = f1_score(y_true=y_gt, y_pred=y_predict)
    return f1


# Please be careful that the input clf need to be trained(after fit training data)
def computeAUC(clf, X_test, y_test, plot=False, plotTitle=""):
    y_score = clf.decision_function(X_test)
#     print('y_score: ',y_score)
    y_test = np.array(y_test)
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)
    
    # plot the figure
    if plot == True:
        plt.plot(fpr, tpr, 'b',label='AUC = %0.2f'% roc_auc)

        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(plotTitle)
        plt.legend(loc="lower right")
#         plt.savefig("/Users/Desktop/" + title + "2.pdf")
        plt.show()

    return roc_auc