#Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

# for the graph
import pydot

col_names = [
	'(0,0)', '(0,1)', '(0,2)',
	'(1,0)', '(1,1)', '(1,2)',
	'(2,0)', '(2,1)', '(2,2)',
	'result'
]

prima = pd.read_csv('ttc.csv', header=None, names=col_names)

# split data into variable and explain
feature_cols = [
	'(0,0)', '(0,1)', '(0,2)',
	'(1,0)', '(1,1)', '(1,2)',
	'(2,0)', '(2,1)', '(2,2)'
]
X = prima[feature_cols] # Features
y = prima.result # Target

# split into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
#print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

export_graphviz(
	clf, 
	out_file= 'decision-tree-ttc.dot',
	feature_names = feature_cols,
	class_names=True,
	node_ids=True, 
    filled=True, 
    rounded=True,
    special_characters=True)






