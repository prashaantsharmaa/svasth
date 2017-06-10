import numpy as np
import csv
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import cross_validation

#feature_file = csv.reader(open('features.txt'), delimiter=" ")
label_file = csv.reader(open('labels.txt'),delimiter = " ")

data_y = []

data_X = np.loadtxt('entropy_roi_features.txt')
print data_X, data_X.shape

for row in label_file:
	data_y.append(row)

data_y = np.array(data_y).astype(np.float)
print data_y.shape,data_y


train_X1 = data_X[0:50,:]
train_X2 = data_X[81:,:]
train_y1 = data_y[0:50,:]
train_y2 = data_y[81:,:]
X_train = np.concatenate((train_X1,train_X2),axis=0)
y_train = np.concatenate((train_y1,train_y2),axis=0)
y_train = y_train.reshape(-1)

X_test = data_X[50:80,:]
y_test = data_y[50:80,:]
y_test = y_test.reshape(-1)
print X_train.shape,y_train.shape
print X_test.shape,y_test.shape
print X_test, y_test

print
print X_test[0] # X_test[0] is ndarray
#X_train , y_train, X_test, y_test = cross_validation.train_test_split(data_X, data_y, test_size = .5, random_state = 0)

#clf = svm.NuSVC(nu=0.2)
#clf = svm.SVC(C=1, kernel='sigmoid', degree=2, gamma=100)
#clf = LogisticRegression(C=1, penalty='l1')
#clf = GradientBoostingClassifier()
#clf = tree.DecisionTreeClassifier()
#clf = AdaBoostClassifier(n_estimators = 1000)
clf =  RandomForestClassifier(n_estimators= 1000)
#clf = GaussianNB()
#clf = MultinomialNB()
#clf = BernoulliNB()
#clf = svm.LinearSVC(C=100000)
clf.fit(X_train,y_train)

print
print "Score of Classifier(Two - Cases)"
print clf.score(X_test,y_test)
print
print "Benign - 0 & Malignant - 1"
print clf.predict(X_test[5].reshape(1,-1))
