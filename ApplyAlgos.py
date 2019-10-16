#firstly use results of feature engineering file
import pandas as pd
train_df=pd.read_csv('train_dataset.csv')
test_df=pd.read_csv('test_dataset.csv')

train_df.interpolate(method='akima',inplace=True)
train_df['bathroom'].fillna(2,inplace=True),train_df['bathroom'].fillna(2,inplace=True)

test_df.interpolate(method='akima',inplace=True)
test_df['location'].fillna(1,inplace=True),test_df['renovation'].fillna(1,inplace=True)

train_df.drop(['Garden','House ID','renovation'],axis=1,inplace=True)
test_df.drop(['Golden Grains','Garden','House ID','renovation'],axis=1,inplace=True)

X_train = train_df.drop("Golden Grains", axis=1)
Y_train = train_df["Golden Grains"]

#Applyinng Linear Regression with cross validation
from time import time
t0=time()
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn import metrics
reg=LinearRegression(normalize=False)
scores=cross_val_score(reg,X_train,Y_train,cv=5,scoring='r2')
print ('mean score is', scores.mean())
print('time required to train by LinearRegression is ',round(time()-t0,2))
print('='*40)

#Applying Lasso Regression
t0=time()
from sklearn.linear_model import LassoCV
reg=LassoCV(max_iter=1500,precompute=True,alphas=[0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.10],selection='random',normalize=True)
reg.fit(X_train,Y_train)
score=reg.score(X_train,Y_train)
print('score is', score)
print('time required to train by LassoRegression is ',round(time()-t0,2))
print('='*40)

#All these things are not important main thing is to apply first data cleaning process and analysing features using various methods and plots.

#Applying Ridge Regression with tuning parameters
t0=time()
from sklearn.linear_model import Ridge
reg= Ridge (alpha = 0.5,max_iter=100,tol=0.00001,random_state=42)
scores=cross_val_score(reg,X_train,Y_train,cv=5,scoring='r2')
print ('mean score is', scores.mean())
print('time required to train by RidgeRegression is ',round(time()-t0,2))
print('='*40)


t0=time()
import xgboost as xgb
#eval_set=[(test_df,labels_test)]
reg = xgb.XGBRegressor(max_depth=3, n_estimators=350, learning_rate=0.1)
#reg.fit(X_train,Y_train,eval_metric="error",eval_set=eval_set,verbose=True)
scores=cross_val_score(reg,X_train,Y_train,cv=5,scoring='r2')
print ('mean score is', scores.mean())
print('time required to train by xgboost is ',round(time()-t0,2))
print('='*40)

#we see xgboost takes higher time than all but gives better accuracy, so can be applied
#giving score of 0.9688484466092451 in 14.7 sec
#trying xgboost without imputation
import pandas as pd
train_df=pd.read_csv('train_dataset.csv')
test_df=pd.read_csv('test_dataset.csv')
train_df.drop(['Garden','House ID','renovation'],axis=1,inplace=True)
test_df.drop(['Golden Grains','Garden','House ID','renovation'],axis=1,inplace=True)

#xgboost is an ensembler. It is much better than adaboost due to it's parallel processing.

X_train = train_df.drop("Golden Grains", axis=1)
Y_train = train_df["Golden Grains"]

t0=time()
import xgboost as xgb
reg = xgb.XGBRegressor(max_depth=3, n_estimators=350, learning_rate=0.1)
scores=cross_val_score(reg,X_train,Y_train,cv=5,scoring='r2')
print ('mean score is', scores.mean())
print('time required to train by xgboost without interpolation is ',round(time()-t0,2))
print('='*40)
#this one gives r2 score of 0.9951203996374514 in 21.5 seconds
#which is best among all so we will use this to test our data

#fitting last algo on train data and plotting importance of various features
reg.fit(X_train,Y_train)
import matplotlib.pyplot as plt
xgb.plot_importance(reg)
plt.show()

#now predicting for test data and comparing with Answers
from sklearn import metrics
pred=reg.predict(test_df)
sol=pd.read_csv('solution.csv')
sol.drop('House ID',axis=1,inplace=True)
score=metrics.r2_score(pred,sol)
print('Final Score is ',score)
