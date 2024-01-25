class RealTimeNotifications:
    def send_notification(self, user_id, message):
        # Send a real-time notification to the user
        print(f"Notification to {user_id}: {message}")

# Example Usage
notifications = RealTimeNotifications()
notifications.send_notification('Zachary', 'Time to hydrate! You haven’t logged water intake in 3 hours.')
