class PersonalityDataIntegration:
    def __init__(self, user_id):
        self.user_id = user_id

    def update_personality_profile(self, personality_data):
        # Process and store the personality data
        print(f"Updated personality profile for user {self.user_id}: {personality_data}")

# Example Usage
user_personality_data = {
    'enneagram_type': 'Type 4',
    'MBTI': 'INFJ',
    'zodiac_sign': 'Pisces'
}
personality_integration = PersonalityDataIntegration(user_id='77821')
personality_integration.update_personality_profile(user_personality_data)
