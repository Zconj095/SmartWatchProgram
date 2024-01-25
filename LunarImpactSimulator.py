import math
class LunarHealthImpactSimulator:
    def __init__(self, birth_phase, current_phase, medication_impact=False):
        self.birth_phase = birth_phase
        self.current_phase = current_phase
        self.medication_impact = medication_impact
        self.health_impacts = {
            'sleep': 0,
            'mood': 0,
            'menstruation': 0,
            'reproduction': 0,
            'cortisol': 0,
            'melatonin': 0
        }

    def calculate_health_impacts(self):
        self._calculate_sleep_impact()
        self._calculate_mood_impact()
        self._calculate_menstruation_and_reproduction_impact()
        self._calculate_hormone_levels()

    def _calculate_sleep_impact(self):
        if self.current_phase == 'full moon':
            self.health_impacts['sleep'] -= 2  # More sleep disturbances
        else:
            self.health_impacts['sleep'] += 1  # Better sleep quality

    def _calculate_mood_impact(self):
        if self.current_phase == 'full moon':
            self.health_impacts['mood'] -= 2  # Increased stress and anxiety
        else:
            self.health_impacts['mood'] += 1  # Improved mood stability

    def _calculate_menstruation_and_reproduction_impact(self):
        # Assuming full moon increases estrogen levels
        if self.current_phase == 'full moon':
            self.health_impacts['menstruation'] = 'increased pain'
            self.health_impacts['reproduction'] = 'increased fertility'

    def _calculate_hormone_levels(self):
        if self.current_phase == 'full moon':
            self.health_impacts['cortisol'] += 1  # Elevated cortisol levels
            self.health_impacts['melatonin'] -= 1  # Reduced melatonin levels

        if self.medication_impact:
            self._adjust_for_medication()

    def _adjust_for_medication(self):
        # Modify impacts based on medication
        self.health_impacts['cortisol'] += 1  # Further modification due to medication
        self.health_impacts['melatonin'] -= 1

    def get_health_impacts(self):
        return self.health_impacts

# Example: A person born during a new moon, currently experiencing a full moon, and on mood-related medication
simulator = LunarHealthImpactSimulator(birth_phase='new moon', current_phase='full moon', medication_impact=True)
simulator.calculate_health_impacts()
print("Health Impacts Based on Lunar Phases:", simulator.get_health_impacts())

class EnhancedLunarHealthImpactSimulator(LunarHealthImpactSimulator):
    def analyze_long_term_trends(self):
        # Analyze data over multiple lunar cycles to identify patterns
        long_term_trends = {}  # Dictionary to store long-term impact trends
        # Logic to analyze long-term trends based on user data
        return long_term_trends

    def suggest_lifestyle_adjustments(self, long_term_trends):
        adjustments = []
        if long_term_trends.get('sleep', 0) < 0:
            adjustments.append("Consider sleep hygiene practices during full moon phases.")
        if long_term_trends.get('mood', 0) < 0:
            adjustments.append("Mindfulness and relaxation techniques can help stabilize mood.")
        # Add more adjustments based on trends
        return adjustments

    def provide_preventive_strategies(self):
        strategies = {
            'full moon': ["Limit exposure to screens", "Practice deep breathing exercises"],
            'new moon': ["Engage in social activities", "Maintain a regular sleep schedule"]
        }
        return strategies.get(self.current_phase, [])

    def coping_strategies_for_medication(self):
        if self.medication_impact:
            return ["Regular check-ins with healthcare provider", "Adjusting medication dosage as per medical advice"]
        return []

enhanced_simulator = EnhancedLunarHealthImpactSimulator(birth_phase='new moon', current_phase='full moon', medication_impact=True)
enhanced_simulator.calculate_health_impacts()

long_term_trends = enhanced_simulator.analyze_long_term_trends()
lifestyle_adjustments = enhanced_simulator.suggest_lifestyle_adjustments(long_term_trends)
preventive_strategies = enhanced_simulator.provide_preventive_strategies()
medication_strategies = enhanced_simulator.coping_strategies_for_medication()

print("Long-term Health Trends:", long_term_trends)
print("Lifestyle Adjustments:", lifestyle_adjustments)
print("Preventive Strategies:", preventive_strategies)
print("Medication Coping Strategies:", medication_strategies)
