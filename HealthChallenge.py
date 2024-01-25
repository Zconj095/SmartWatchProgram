class HealthChallenge:
    def __init__(self, challenge_name, goal, duration):
        self.challenge_name = challenge_name
        self.goal = goal
        self.duration = duration
        self.participants = []

    def join_challenge(self, user):
        # User joins a health challenge
        self.participants.append(user)
        print(f"{user.name} has joined the {self.challenge_name} challenge!")

    def track_progress(self, user):
        # Track user's progress in the challenge
        # Placeholder for tracking logic
        progress = "50% completed"
        return f"{user.name}'s Progress: {progress}"

# Example Usage
step_challenge = HealthChallenge("10,000 Steps a Day", 10000, "30 Days")
step_challenge.join_challenge(user)
print(step_challenge.track_progress(user))

