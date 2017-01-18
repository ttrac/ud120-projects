#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import tree
from sklearn.metrics import accuracy_score


### decision tree A/B
# print "\nbuilding decision tree A..."
# clf_a = tree.DecisionTreeClassifier(min_samples_split=2)
# clf_a.fit(features_train, labels_train)
# pred_a = clf_a.predict(features_test)

# acc_min_samples_split_2 = accuracy_score(pred_a, labels_test)
# print "accuracy for split=2:", round(acc_min_samples_split_2, 3)

### decision tree final quiz
print "\nstart decision tree..."
clf = tree.DecisionTreeClassifier(min_samples_split=40)
print "\nnumber of features:", len(features_train[0])
print "\ntraining in progress..."
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

acc = accuracy_score(pred, labels_test)
print "accuracy:", round(acc, 3)


#########################################################


