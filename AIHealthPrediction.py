class AIHealthPrediction:
    def __init__(self, user_health_data):
        self.user_health_data = user_health_data

    def make_predictions(self):
        # Analyze health data and predict future health scenarios
        if self.user_health_data['blood_pressure'] > 140:
            return "Risk of hypertension identified. Suggested action: Regular monitoring and consultation."
        return "No immediate health risks identified."

# Example Usage
user_health_data = {'blood_pressure': 145, 'heart_rate': 80}
ai_prediction = AIHealthPrediction(user_health_data)
print(ai_prediction.make_predictions())