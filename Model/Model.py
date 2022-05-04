import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
import pickle


# Save new cleane data in a Datafream
df=pd.read_csv("New-ImmoElliza.csv")

# drop column 'Unnamed:0'
df = df.drop(['Unnamed: 0'], axis = 1)

# Selecting independent variable
X= df.iloc[:,2:]

#Selecting dependent variable
y= df.iloc[:,1]

# Splitting data into train and test split

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

# feature scaling:standarding the dataset
from sklearn.preprocessing import StandardScaler 

# fitting  and transforming the training dataset.
st_x= StandardScaler()  
X_train= st_x.fit_transform(X_train)

# fitting  and transforming the test dataset
X_test= st_x.transform(X_test)

#fixed import
from sklearn.preprocessing import MinMaxScaler 
scaler = MinMaxScaler()
X_train= scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create linear regression object
regr = linear_model.LinearRegression()

#Train the model using the training sets
regr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = regr.predict(X_test)

# Saving model to disk
pickle.dump(regr, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))




