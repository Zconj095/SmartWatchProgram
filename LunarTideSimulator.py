class LunarTideSimulator:
    def __init__(self, moon_earth_distance, sun_moon_alignment):
        self.moon_earth_distance = moon_earth_distance
        self.sun_moon_alignment = sun_moon_alignment  # 'aligned' or 'right angle'

    def calculate_lunar_tide_strength(self):
        # The tide strength is inversely proportional to the cube of the distance
        tide_strength = 1 / (self.moon_earth_distance ** 3)
        return tide_strength

    def determine_tide_type(self):
        # Spring tides occur when the Sun and Moon are aligned
        # Neap tides occur when the Sun and Moon are at right angles
        if self.sun_moon_alignment == 'aligned':
            return 'Spring Tide'
        elif self.sun_moon_alignment == 'right angle':
            return 'Neap Tide'
        else:
            return 'Regular Tide'

    def simulate_tide(self):
        lunar_tide_strength = self.calculate_lunar_tide_strength()
        tide_type = self.determine_tide_type()
        return f"Lunar tide strength: {lunar_tide_strength}, Tide type: {tide_type}"

# Example usage of the LunarTideSimulator
# Assuming moon_earth_distance is in Earth-Moon distances (EMD) and sun_moon_alignment is a string
simulator = LunarTideSimulator(moon_earth_distance=1, sun_moon_alignment='aligned')
tide_info = simulator.simulate_tide()
print(tide_info)