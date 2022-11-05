
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# Loading The Network Anomaly Detection Dataset
NADdataset = pd.read_csv("dataset.csv")
print('The Numer of Row And Cloumns is:', NADdataset.shape)
#print('First 5 Rows Of The Dataset    ' , NADdataset.head(5))

# check for Missing Value
#print(NADdataset.isnull().sum())

print()
print()
# statistical measues of the dataset
#print(NADdataset.describe())

"""
# Number of values for each quality
print(sns.catplot(x='class',data=NADdataset,kind='count'))


plot =  plt.figure(figsize=(5,5))
print(sns.barplot(x='class',y='ifInOctets11',data=NADdataset))


# Correlation
#1) Positiive correlation
#2) Negative  correlation
correlation = NADdataset.corr()
plt.figure(figsize=(10,10))
print(sns.heatmap(correlation,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blues'))

"""
# Data Preprocessing
# spreate the data Label


X = NADdataset.iloc[:,:1]
Y = NADdataset.iloc[:, -1]
#print(X)
#print(Y)

x_train , x_test , y_train , y_test = train_test_split(X,Y,test_size=0.3 , random_state=2)

print(X.shape,Y.shape,y_train.shape,y_test.shape)

#Traning Our Model Random Forest


model = RandomForestClassifier(n_estimators=100)
model.fit(x_train,y_train)

# Accurecy Score

x_test_pre =  model.predict(x_test)
test_data_acu =  accuracy_score(x_test_pre,y_test)

print("Acureccy " ,test_data_acu)

# bulid Predection System


input_data =  (2257767832,907308930,0,52287097,17015,0,7291152,3975,1,701,552,51,14,2,5,3,241978,187854,1,22,59638909,245955,188475,569,23,59581345,7,0,51,27,47,23,24,24)
# changing the input data to numpy array

input_data_nparry = np.asarray(input_data)
#reshape the numpy array aw we .......
# for particluar instaice
input_date_reshape =  input_data_nparry.reshape(34,-1)
prediection   = model.predict(input_date_reshape)

print(prediection)





