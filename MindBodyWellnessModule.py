class MindBodyWellnessModule:
    def recommend_routine(self, user_data):
        # Recommend a mind-body wellness routine based on user data
        if user_data['stress_level'] > 7:
            return "High stress detected. Recommended routine: 15-minute guided mindfulness meditation."
        return "Stress levels normal. Recommended routine: 30-minute gentle yoga session."

# Example Usage
user_data = {'stress_level': 8, 'physical_activity': 'moderate'}
mind_body_module = MindBodyWellnessModule()
print(mind_body_module.recommend_routine(user_data))