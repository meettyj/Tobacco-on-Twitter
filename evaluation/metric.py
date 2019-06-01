import numpy as np
from sklearn.metrics import f1_score

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