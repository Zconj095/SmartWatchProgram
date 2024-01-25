class HealthRecommendationAI:
    def __init__(self, user_health_data):
        self.user_health_data = user_health_data

    def generate_recommendations(self):
        # AI logic for generating health recommendations
        # Example placeholder logic
        if self.user_health_data['sleep_quality'] < 50:
            return "Recommendation: Consider adopting a pre-sleep relaxation routine to improve sleep quality."
        else:
            return "Your sleep quality is good. Keep maintaining your current routine."

# Example Usage
user_health_data = {'sleep_quality': 45, 'activity_level': 'moderate'}
recommendation_ai = HealthRecommendationAI(user_health_data)
print(recommendation_ai.generate_recommendations())