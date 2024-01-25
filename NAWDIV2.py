class NutritionAnalyzerV2:
    # Second version of NutritionAnalyzer
    def __init__(self, nutritional_data):
        self.nutritional_data = nutritional_data

    def analyze_macros(self):
        feedback = []
        if self.nutritional_data.get('protein') < 50:
            feedback.append("Protein intake is low. Consider incorporating more lean protein sources.")
        if self.nutritional_data.get('carbs') > 300:
            feedback.append("Carb intake is high. Consider reducing sugary foods.")
        return feedback

class WearableDeviceIntegrationV2:
    # Second version of WearableDeviceIntegration
    def __init__(self):
        self.steps = 0
        self.heart_rate = 0
        self.sleep_quality = 0

    def sync_data(self):
        self.steps = 12000
        self.heart_rate = 72
        self.sleep_quality = 80

    def get_data(self):
        return {
            'Steps': self.steps,
            'Heart Rate': self.heart_rate,
            'Sleep Quality': self.sleep_quality
        }