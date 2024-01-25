class HealthDataAnalyzer:
    def __init__(self, health_data):
        self.health_data = health_data

    def analyze_mental_wellness(self):
        # Placeholder logic for mental wellness analysis
        stress_level = self.health_data.get('stress_level', 0)
        mood = self.health_data.get('mood', 'neutral')
        return f"Stress Level: {stress_level}, Mood: {mood}"

    def analyze_environmental_factors(self):
        # Placeholder logic for environmental factor analysis
        air_quality = self.health_data.get('air_quality', 'good')
        return f"Air Quality: {air_quality}"

# Example Usage
health_data = {'stress_level': 3, 'mood': 'content', 'air_quality': 'moderate'}
health_data_analyzer = HealthDataAnalyzer(health_data)
print(health_data_analyzer.analyze_mental_wellness())
print(health_data_analyzer.analyze_environmental_factors())
