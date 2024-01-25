import NutritionAnalyzer
import HealthDashboard
from NAWDIV2 import WearableDeviceIntegrationV2
from MPCBIOWDI import * 
class CentralHealthSystem:
    def __init__(self, user_profile, nutritional_data, wearable_device):
        self.user_profile = user_profile
        self.nutrition_analyzer = NutritionAnalyzer(nutritional_data)
        self.wearable_device = WearableDeviceIntegrationV2()
        self.health_dashboard = HealthDashboard({})  # Initialize with empty data

    def update_system(self):
        # Synchronize data from wearable device
        # Analyze nutritional data
        health_data = self.wearable_device.get_data()
        wearable_data = self.wearable_device.get_data()
        nutrition_feedback = self.nutrition_analyzer.analyze_macros()
        # Example logic to update the system
        # Update health dashboard with new data
        self.health_dashboard.user_health_data = {
            'Profile': self.user_profile,
            'Wearable Data': wearable_data,
            'User Profile': self.user_profile,
            'Health Data': health_data,
            'Nutrition Feedback': nutrition_feedback
            
        }
        
    def generate_health_report(self):
        health_data = self.wearable_device.get_data()
        wearable_data = self.wearable_device.get_data()
        # Analyze nutritional data
        nutrition_feedback = self.nutrition_analyzer.analyze_macros()


        return {
            'Profile': self.user_profile,
            'Wearable Data': wearable_data,
            'User Profile': self.user_profile,
            'Health Data': health_data,
            'Nutrition Feedback': nutrition_feedback
        }


    def display_dashboard(self):
        self.health_dashboard.display()
    # Assuming WearableDeviceIntegrationV2 is already defined as discussed earlier
        wearable_device = WearableDeviceIntegrationV2()

    # Now you can create an instance of CentralHealthSystem with the wearable_device
    nutritional_data = {
        'calories': 2000,
        'protein': 50,
        'carbs': 250,
        'fats': 70,
        # ... other nutritional data ...
    }
    user_profile = {
        'name': 'Zachary Confer',
        'age': 28,
        # ... other profile information ...
central_system = CentralHealthSystem(user_profile, nutritional_data, wearable_device)
central_system.update_system()
central_system.display_dashboard()
wearable_device = WearableDeviceIntegration()
print(central_system.generate_health_report())

    }




