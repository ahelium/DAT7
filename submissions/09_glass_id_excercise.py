'''
EXERCISE: Glass Identification (aka "Glassification")
'''

# TASK 1: read the data into a DataFrame
import pandas as pd
data = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data',header=0, names=names)
names = ['Id', 'RI','Na','Mg','Al','Si','K','Ca','Ba','Fe','Type']

# TASK 2: briefly explore the data
data.head()
data.describe()
# TASK 3: convert into binary classification problem

data['binary'] = [0 if row in [1,2,3,4] else 1 for row in data['Type']]

# TASK 4: create a feature matrix (X) using all features
feature_names = ['RI','Na','Mg','Al','Si','K','Ca','Ba','Fe']
X = data[feature_names]
X.shape

# TASK 5: create a response vector (y)
y = data['binary']

# TASK 6: split X and y into training and testing sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)

# TASK 7: fit a KNN model on the training set using K=5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)


# TASK 8: make predictions on the testing set and calculate testing accuracy
knn.predict(X_test)

# TASK 9: write a for loop that computes testing accuracy for a range of K values

from sklearn import metrics

k_range = range(1,31)
training_error = []
testing_error = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    testing_error.append(1 - metrics.accuracy_score(y_test, y_pred))



# TASK 10: plot K value versus testing accuracy to choose on optimal value for K
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.plot(k_range, testing_error)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Error')

df = pd.DataFrame({'K': k_range, 'train':training_error, 'test':testing_error}).set_index('K')
df.head()
df.plot()

# TASK 11: calculate the null accuracy

# TASK 12: search for useful features

# redo exercise using only those features
