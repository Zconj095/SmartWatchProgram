import HealthDashboard
import CentralHealthSystem
class UserInteractivity:
    def set_goal(self, user, goal):
        print(f"Setting goal for {user}: {goal}")

    def track_progress(self, user):
        return f"Tracking progress for {user}"

# Example usage of the updated classes
central_system = CentralHealthSystem(user_profile={'name': 'Zachary', 'age': 28}, nutritional_data={'calories': 1800, 'protein': 55, 'carbs': 250, 'fats': 60}, wearable_device=WearableDeviceIntegrationV2())
central_system.update_system()
central_system.display_dashboard()

user_interactivity = UserInteractivity()
user_interactivity.set_goal('Zachary', '10000 steps daily')
print(user_interactivity.track_progress('Zachary'))


# Example Usage
user_health_data = {'Biorhythms': 'Balanced', 'Hormone Levels': 'Normal', 'Nutrition': 'Caloric intake high'}
health_dashboard = HealthDashboard(user_health_data)
health_dashboard.display()
