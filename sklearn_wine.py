import numpy as np 
import pandas as pd 

from sklearn.model_selection import train_test_split 
from sklearn import preprocessing 
from sklearn.ensemble import RandomForestRegressor 

#cross validation toos 
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

#evaluation metrics 
from sklearn.metrics import mean_squared_error, r2_score

#save the trained model, Model persistence
from sklearn.externals import joblib

dataset_url = 'http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
#separating the data into a standarised format
data = pd.read_csv(dataset_url,sep=';')

#making a model to predict the quality of wine
#splitting the data on quality
y=data.quality
x=data.drop('quality',axis=1)

#splitting the data into training and test with 20% as test data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=123,stratify=y)

#scaling the data using preprocessing library
#without it we would minus the mean and divide by the standard deviation
#using pipeline to make a pipeline between the model and the standard Scaler
pipeline=make_pipeline(preprocessing.StandardScaler(),RandomForestRegressor(n_estimators=100))
#setting the hyperparameters
hyperparameters =  {'randomforestregressor__max_features':['auto','sqrt','log2'],'randomforestregressor__max_depth':[None,5,3,1]}
#using cross validation to select the right parameters. Using GraphCV searches and fits the proper data
clf=GridSearchCV(pipeline,hyperparameters,cv=10) #1 hold out and 9 train, iterated over 10 times
#training to avoid overfitting and choosing optimal parameter
clf.fit(x_train,y_train)
#clf.best_params_  #displays the optimal chosen parameters

#using the model to predict the test data
y_pred=clf.predict(x_test)

#finding the error in the predictions
print(r2_score(y_test,y_pred))
print(mean_squared_error(y_test,y_pred))

#saving the trained model for future use in pkl format
joblib.dump(clf,'randomForest_regressor_wine.pkl')
#to load: clf = joblib.load('randomForest_regressor_wine.pkl')









