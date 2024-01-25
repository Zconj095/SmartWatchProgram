import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Example function to train a classification model
def train_health_risk_model(data):
    X = data.drop('risk_label', axis=1)
    y = data['risk_label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier()  # or GradientBoostingClassifier()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    print(f"Model Accuracy: {accuracy_score(y_test, predictions)}")
    return model

# Example function to train a time series model for trend prediction
def train_trend_prediction_model(time_series_data):
    model = ARIMA(time_series_data, order=(5,1,0))
    model_fit = model.fit()
    return model_fit

