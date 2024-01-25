class SolarTideSimulator:
    def __init__(self, sun_earth_distance, moon_phase):
        self.sun_earth_distance = sun_earth_distance
        self.moon_phase = moon_phase

    def calculate_solar_tide_strength(self):
        # The tide strength is inversely proportional to the cube of the distance
        tide_strength = 1 / (self.sun_earth_distance ** 3)
        return min(tide_strength, 0.5)  # Limiting to half the strength of lunar tides

    def combine_with_moon_phase(self):
        # Spring tides occur when the Sun and Moon are aligned (new moon or full moon)
        # Neap tides occur when the Sun and Moon are at right angles (first or last quarter)
        if self.moon_phase in ['new moon', 'full moon']:
            return 'Spring Tide'
        elif self.moon_phase in ['first quarter', 'last quarter']:
            return 'Neap Tide'
        else:
            return 'Regular Tide'

    def simulate_tide(self):
        solar_tide_strength = self.calculate_solar_tide_strength()
        tide_type = self.combine_with_moon_phase()
        return f"Solar tide strength: {solar_tide_strength}, Tide type: {tide_type}"

# Example usage of the SolarTideSimulator
# Assuming sun_earth_distance is in astronomical units (AU) and moon_phase is a string
simulator = SolarTideSimulator(sun_earth_distance=1, moon_phase='full moon')
tide_info = simulator.simulate_tide()
print(tide_info)