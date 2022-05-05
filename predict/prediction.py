import tracemalloc
import pandas as pd
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
#from sklearn.metrics import accuracy_score
#from sklearn.metrics import balanced_accuracy_score
#from sklearn.metrics import recall_score
#from sklearn.metrics import precision_score
#from sklearn.metrics import f1_score
import pickle



def train():

    # Save new cleaned data in a Datafream
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

    '''# feature scaling:standarding the dataset
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
    X_test = scaler.transform(X_test)'''

    # Create linear regression object
    regr = linear_model.LinearRegression()

    print(X_train)

    #Train the model using the training sets
    regr.fit(X_train, y_train)

    # Saving model to disk
    pickle.dump(regr, open('model.pkl','wb'))

    
def predict(mylist):

    # Loading model to compare the results
    model = pickle.load(open('model.pkl','rb'))
    # print(mylist)

    # arr = np.array([12, 23, 45, 67, 78])
    # pred = model.predict([arr])
    
    # Make prediction using model loaded from disk as per the data.
    # prediction = model.predict([np.array(mylist).reshape(1, -1)])
    prediction = model.predict([np.array(mylist)])
    
     
    return prediction[0]

#dic={"house_surface":1235,"house_bedroom":6,"house_attic":0,"house_terrace":1,"house_swimmingpool":1}

#prediction=predict(list(dic.values()))
#train()
#print(prediction)
