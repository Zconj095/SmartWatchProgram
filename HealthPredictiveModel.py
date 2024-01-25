from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

class HealthPredictiveModel:
    def __init__(self, historical_data):
        self.historical_data = historical_data
        self.model = RandomForestClassifier()

    def train_model(self):
        # Train the model on historical data
        X_train, X_test, y_train, y_test = train_test_split(self.historical_data['features'], self.historical_data['labels'], test_size=0.2)
        self.model.fit(X_train, y_train)

    def predict(self, new_data):
        # Predict future health trends
        return self.model.predict(new_data)