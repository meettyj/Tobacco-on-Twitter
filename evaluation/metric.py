import numpy as np
from sklearn.metrics import f1_score
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
from sklearn.preprocessing import label_binarize
from scipy import interp

def computeAccuracy(y_predict, y_gt):
# comps = y_test[:100] != pred_alc_new[:100]
    comps = y_gt != y_predict
    # print(comps[:100])
    print('length of total comps: ', len(comps))
    diff = list(np.where(comps)[0])
    # print('length of difference: ', len(diff))
    # print(diff)
    print('%d different item in whole dataset'%(len(diff)))
    acc = (len(comps)-len(diff))/len(comps)*100
    print('accuracy: %f%%'%(acc))
    return acc


def computeF1Score(y_gt, y_predict, average='binary'):
# average : string, [None, ‘binary’ (default), ‘micro’, ‘macro’, ‘samples’, ‘weighted’]

#     kwargs = {}
#     kwargs["average"] = 'micro'
#     f1 = f1_score(y_true=y_gt, y_pred=y_alc_initial, **kwargs)
    f1 = f1_score(y_true=y_gt, y_pred=y_predict, average=average)
    return f1


# Please be careful that the input clf need to be trained(after fit training data)
def computeAUC(clf, X_test, y_test, plot=False, plotTitle="", RF=False):
    if RF == False:
        y_score = clf.decision_function(X_test)
    else:
        # make sure take the prediction probalibity of class 1.
        y_score = clf.predict_proba(X_test)[:,1]
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



def computeAUCBehavior(clf, X_test, y_test, plot=False, plotTitle="", RF=False):
    class2name= ["current", "looking", "reflecting"]
    if RF == False:
        y_score = clf.decision_function(X_test)
    else:
        # make sure take the prediction probalibity of class 1.
        y_score = clf.predict_proba(X_test)
#     print('y_score[1]: ', y_score[1]) # should be 3

    y_test = label_binarize(np.array(y_test), [0,1,2])
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    # n_classes = len(y_score[1])
    n_classes = 3
#     print('n_class: ', n_classes)
#     y_test = np.array(y_test)
#     print('y_test: ', type(y_test))
    for i in range(n_classes):
        y_test = np.array(y_test)
        fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
#         print(class2name[i])
        roc_auc[class2name[i]] = auc(fpr[i], tpr[i])

    # Compute micro-average ROC curve and ROC area
    fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
    roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

    # Compute macro-average ROC curve and ROC area
    # First aggregate all false positive rates
    all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

    # Then interpolate all ROC curves at this points
    mean_tpr = np.zeros_like(all_fpr)
    for i in range(n_classes):
        mean_tpr += interp(all_fpr, fpr[i], tpr[i])

    # Finally average it and compute AUC
    mean_tpr /= n_classes
    fpr["macro"] = all_fpr
    tpr["macro"] = mean_tpr
    roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

    
    if plot == True:
        # Plot all ROC curves
        plt.figure()
        plt.plot(fpr["micro"], tpr["micro"],
                 label='micro-average ROC (area = {0:0.2f})'
                       ''.format(roc_auc["micro"]),
                 linewidth=2)
        plt.plot(fpr["macro"], tpr["macro"],
                 label='macro-average ROC (area = {0:0.2f})'
                       ''.format(roc_auc["macro"]),
                 linewidth=2)

        for i in range(n_classes):
            plt.plot(fpr[i], tpr[i], label='{0} ROC (area = {1:0.2f})'
                                           ''.format(class2name[i], roc_auc[class2name[i]]))

        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Behavior Level ROC')
        plt.legend(loc="lower right")
    #     plt.savefig("/Users/Eddie/Desktop/plt_roc_fpl.pdf")
        plt.show()

    return roc_auc









