class BrainwaveAnalyzer:
    def __init__(self, data):
        self.data = data  # EEG data or simulated data

    def categorize_brainwaves(self):
        categorized_data = {'Delta': [], 'Theta': [], 'Alpha': [], 'Beta': [], 'Gamma': []}
        for frequency in self.data:
            if 0.5 <= frequency <= 4:
                categorized_data['Delta'].append(frequency)
            elif 4 < frequency <= 8:
                categorized_data['Theta'].append(frequency)
            elif 8 < frequency <= 12:
                categorized_data['Alpha'].append(frequency)
            elif 12 < frequency <= 30:
                categorized_data['Beta'].append(frequency)
            elif frequency > 30:
                categorized_data['Gamma'].append(frequency)
        return categorized_data

    def analyze_implications(self, categorized_data):
        implications = {}
        if categorized_data['Delta']:
            implications['Delta'] = 'Deep sleep or unconsciousness'
        if categorized_data['Theta']:
            implications['Theta'] = 'Drowsiness, meditation, daydreaming'
        if categorized_data['Alpha']:
            implications['Alpha'] = 'Relaxation, alertness, calmness'
        if categorized_data['Beta']:
            implications['Beta'] = 'Wakefulness, focus, concentration'
        if categorized_data['Gamma']:
            implications['Gamma'] = 'Higher cognitive functions'
        return implications
