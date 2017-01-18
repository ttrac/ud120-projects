#!/usr/bin/python

# import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from time import time
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


### Create and fit an AdaBoosted decision tree

# clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=100),
#                          algorithm="SAMME",
#                          n_estimators=20000)

clf = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=2),
    n_estimators=10000,
    learning_rate=1.8,
    algorithm="SAMME.R")

print "\nstart AdaBoost decision tree..."
print "\ntraining in progress..."
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
# print "\nnumber of features:", len(features_train[0])

print "\npredicting in progress..."
t1 = time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"




acc = accuracy_score(pred, labels_test)
print "accuracy:", round(acc, 3)



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
