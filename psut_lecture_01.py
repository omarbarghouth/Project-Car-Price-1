# -*- coding: utf-8 -*-
"""PSUT LECTURE 01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wentcfv9WFugyl3ht_Act1OZu9e9tpE_
"""

import pandas as pd

melbourne_data = pd.read_csv("/content/sample_data/melb_data.csv")
#melbourne_data.columns

y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))

import pandas as pd
df = pd.read_csv("/content/sample_data/car_price_prediction.csv")
#melbourne_data.columns
df = df.dropna(axis=0)
df.describe()

y=df.Price

df_features=['ID','Cylinders','Airbags']

X = df[df_features]
from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
df_model = DecisionTreeRegressor(random_state=1)

# Fit model
df_model.fit(X,y)
print("Making predictions for the following 5 Cars:")
print(X.head())
print("The predictions are")
print(df_model.predict(X.head()))


from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# Define model
melbourne_model = DecisionTreeRegressor()
# Fit model
melbourne_model.fit(train_X, train_y)

# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))