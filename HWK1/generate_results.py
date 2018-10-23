import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.LDA import LDA
from utils.LogisticRegression import LogisticRegression
from utils.LinearRegression import LinearRegression
from utils.QDA import QDA
import numpy as np

SEED = 17

train_A = pd.read_table("data/classificationA.train", header=None)
train_B = pd.read_table("data/classificationB.train", header=None)
train_C = pd.read_table("data/classificationC.train", header=None)
test_A = pd.read_table("data/classificationA.test", header=None)
test_B = pd.read_table("data/classificationB.test", header=None)
test_C = pd.read_table("data/classificationC.test", header=None)
train_A = train_A.values
train_B = train_B.values
train_C = train_C.values
test_A = test_A.values
test_B = test_B.values
test_C = test_C.values

train = {'A': train_A, 'B': train_B, 'C': train_C}
test = {'A': test_A, 'B': test_B, 'C': test_C}
missclassification = {'A':{}, 'B':{}, 'C':{}}
for val in missclassification.values() :
    val.update({'train':{}, 'test':{}})

for key in ['A', 'B', 'C']:
    X_train = train[key][:,:2]
    y_train = train[key][:,-1]
    X_test = test[key][:,:2]
    y_test = test[key][:,-1]
    lda = LDA()
    logreg = LogisticRegression()
    linreg = LinearRegression()
    qda = QDA()
    clf = {'LDA': lda,
           'Logistic Regression': logreg,
           'Linear Regression': linreg,
           'QDA': qda}
    for clf_key in clf.keys():
        np.random.seed(SEED)
        clf[clf_key].fit(X_train, y_train)

        error = clf[clf_key].missclassification(X_train, y_train)
        missclassification[key]['train'][clf_key] = error
        title = clf_key + r" $\times$ Dataset " + key + " - train - error rate="+str(round(100*error,3)) + "%"
        clf[clf_key].plot_pred(X_train, y_train, title=title)
        save_path = "_".join(["docs/img/"+clf_key, key, "train.png"])
        plt.savefig(save_path)
        plt.close()

        error = clf[clf_key].missclassification(X_test, y_test)
        missclassification[key]['test'][clf_key] = error
        title = clf_key + r" $\times$ Dataset " + key + " - test - error rate="+str(round(100*error,3)) + "%"
        clf[clf_key].plot_pred(X_test, y_test, title=title)
        save_path = "_".join(["docs/img/"+clf_key, key, "test.png"])
        plt.savefig(save_path)
        plt.close()

        missclassification_df = pd.DataFrame(missclassification[key])
        missclassification_df = 100*missclassification_df
        missclassification_df = missclassification_df.round(3)
        missclassification_df.to_latex("docs/tex/missclassification_" + key + ".tex")
