#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

# fit the classifier using the training features/labels
# make a set of predictions on the test data
# store your predictions in a list named pred

### your code goes here ###

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


features_train, features_test, labels_train, labels_test = preprocess()

features_train = features_train[:len(features_train)/100] 
labels_train = labels_train[:len(labels_train)/100] 

clf = SVC(kernel="rbf", C=10000)

t0 = time()
print "training in progress..."
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
print "predicting in progress..."
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

# calculate accuracy
acc = accuracy_score(pred, labels_test)
print "accuracy_score:", acc

print "--- SPECIFIC PREDICTIONS ---"
print "pred[10] =", pred[10]
print "pred[26] =", pred[26]
print "pred[50] =", pred[50]
# print "pred[10] =", clf.predict(features_train[10])
# print "pred[25] =", clf.predict(features_train[25])
# print "pred[50] =", clf.predict(features_train[50])

print "--- COUNTS ---"
from collections import Counter
print "Counter =", Counter(pred)
print "sum(pred) =", sum(pred)

#########################################################


