import datetime
import ephem
import random
import SCCBIOCHL

import matplotlib.pyplot as plt
def get_moon_phase(date):
    observer = ephem.Observer()
    observer.date = date.strftime("%Y/%m/%d")
    moon = ephem.Moon(observer)
    moon_phase_number = moon.phase / 100

    if moon_phase_number == 0:
        return "New Moon"
    elif 0 < moon_phase_number <= 0.25:
        return "Waxing Crescent"
    elif 0.25 < moon_phase_number <= 0.5:
        return "First Quarter"
    elif 0.5 < moon_phase_number <= 0.75:
        return "Waxing Gibbous"
    elif 0.75 < moon_phase_number < 1:
        return "Full Moon"
    elif 1 > moon_phase_number > 0.75:
        return "Waning Gibbous"
    elif 0.75 > moon_phase_number > 0.5:
        return "Last Quarter"
    elif 0.5 > moon_phase_number > 0:
        return "Waning Crescent"

def calculate_biorhythms(date):
    moon_phase = get_moon_phase(date)
    sun_cycle_phase = get_sun_cycle_approx(date)
    
    print(f'Date: {date}')
    print(f'Moon Phase: {moon_phase}')   
    print(f'Sun Cycle Phase: {sun_cycle_phase}') 

class NutritionAnalyzerV1:
    # Renamed from NutritionAnalyzer
    def __init__(self, nutritional_data):
        self.nutritional_data = nutritional_data

    def analyze(self):
        if self.nutritional_data.get('calories') > 2000:
            return "Caloric intake is high. Consider reducing calorie-rich foods."
        else:
            return "Caloric intake is within recommended limits."

class WearableDeviceIntegration:
    # Renamed from WearableDeviceIntegration
    def __init__(self):
        self.steps = 0
        self.heart_rate = 0
        self.sleep_quality = 0  # New metric

    def sync_data(self):
        # Simulate real-time data synchronization
        self.steps = 12000
        self.heart_rate = 72
        self.sleep_quality = 80  # Assuming 100 is best
    def get_data(self):
        return {
            'Steps': self.steps,
            'Heart Rate': self.heart_rate,
            'Sleep Quality': self.sleep_quality
        }

# Example Usage
wearable_device = WearableDeviceIntegration()
wearable_device.sync_data()
print(wearable_device.get_data())


# Example usage
test_date = datetime.datetime(2024, 1, 20)
print(get_moon_phase(test_date))
