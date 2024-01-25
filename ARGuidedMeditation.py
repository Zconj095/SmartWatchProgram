class ARGuidedMeditation:
    def start_session(self, user_preferences):
        print(f"Starting AR-guided meditation session with settings: {user_preferences}")

    def adjust_session(self, adjustments):
        print(f"Adjusting meditation session: {adjustments}")

# Example Usage
ar_meditation = ARGuidedMeditation()
user_preferences = {'environment': 'beach', 'session_length': '15 minutes'}
ar_meditation.start_session(user_preferences)
ar_meditation.adjust_session({'session_length': '20 minutes'})
