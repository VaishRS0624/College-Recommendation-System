import pandas as pd
# from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
# from sklearn import metrics
# import matplotlib.pyplot as plt

# Assuming you have a DataFrame named 'df' with your data

class aimodel:
    def trainmodel(self,inn):
        df = pd.read_csv('train.csv')

# Split the data into features (X) and target variable (y)
        X = df[['cutoffrank', 'cutoffscore']]
        y = df['choicecode']

# Split the data into training and testing sets
        numeric_y = pd.get_dummies(y, drop_first=True)
# Create a linear regression model
        model = LinearRegression()

# Fit the model to the training data
        model.fit(X, numeric_y)

# Make predictions on the test set
#         y_pred = model.predict(X)

# Print the coefficients
        print('Coefficients:', model.coef_)

        # inn = input('enter value of rank and score')

# Convert the string to a list of integers
#         inn_list = list(map(int, inn.split()))

# Reshape the list to a 2D array
        inn_array = np.array(inn).reshape(1, -1)
        print(inn_array)

# Make predictions
        ypredicted = model.predict(inn_array)

        print('Predicted choice code:', ypredicted)

        predicted_index = np.argmax(ypredicted)

# Retrieve the corresponding choice code
        predicted_choice_code = df['choicecode'].iloc[predicted_index]

        print('Predicted choice code:', predicted_choice_code)

        top_n_indices = np.argsort(ypredicted[0])[::-1][:20]  # Change N to the number of top choices you want

# Retrieve the corresponding choice codes and probabilities
        top_n_choice_codes = df['choicecode'].iloc[top_n_indices]
        top_n_probabilities = ypredicted[0][top_n_indices]
        list1=[]
# Print the results
        for code, prob in zip(top_n_choice_codes, top_n_probabilities):
            list1.append(code)

        print(f'Choice Code: {code}, Probability: {prob}')

        print(list1)
        return list1

# a1=aimodel()
# listodchoices=a1.trainmodel(['80','100'])