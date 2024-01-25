class GoalSettingAndTracking:
    def __init__(self):
        self.user_goals = {}

    def set_goal(self, user_id, goal):
        self.user_goals[user_id] = goal
        print(f"Goal set for {user_id}: {goal}")

    def track_goal_progress(self, user_id):
        # Placeholder for tracking logic
        return f"Progress for {user_id}'s goal: 50% achieved"

# Example Usage
goal_tracker = GoalSettingAndTracking()
goal_tracker.set_goal('Zachary', 'Walk 5mi in under 1hr minutes')
print(goal_tracker.track_goal_progress('Zachary'))