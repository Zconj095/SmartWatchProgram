class ThirdPartyAppIntegration:
    def __init__(self, app_name):
        self.app_name = app_name

    def sync_data(self, user_id):
        # Placeholder for data synchronization logic with the app
        return f"Data synchronized from {self.app_name} for user {user_id}"

# Example Usage
cashwalk_integration = ThirdPartyAppIntegration("Cashwalk")
print(cashwalk_integration.sync_data(user_id="77821"))
