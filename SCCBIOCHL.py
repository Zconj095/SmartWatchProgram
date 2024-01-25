from MPCBIOWDI import test_date
from MPCBIOWDI import get_moon_phase
from SGBIOCBIO import get_circadian_tendency
from SGBIOCBIO import get_season
def get_sun_cycle_approx(current_date):
    """
    Approximate the solar cycle phase based on the current date.
    This is a simplified method and may not be highly accurate.
    """
    # Approximate length of the solar cycle in years
    solar_cycle_length = 11

    # A recent solar cycle began in 2020
    cycle_start_year = 2020

    # Calculate the current year in the cycle
    year_in_cycle = (current_date.year - cycle_start_year) % solar_cycle_length

    # Determine the sun cycle phase
    if year_in_cycle < 3:
        return "Rising Phase"
    elif 3 <= year_in_cycle < 5:
        return "Solar Maximum"
    elif 5 <= year_in_cycle < 8:
        return "Declining Phase"
    else:
        return "Solar Minimum"

# Test the function with the current date
get_sun_cycle_approx(test_date)

def calculate_biorhythms(date, birth_date, birth_time):
    season = get_season(date)
    moon_phase = get_moon_phase(date)
    sun_cycle_phase = get_sun_cycle_approx(date)
    circadian_tendency = get_circadian_tendency(birth_time)
    
    # Print out calculated cycles
    print(f'Date: {date}')
    print(f'Season: {season}')
    print(f'Moon Phase: {moon_phase}')   
    print(f'Sun Cycle Phase: {sun_cycle_phase}')
    print(f'Circadian Tendency: {circadian_tendency}') 

# Example usage
birth_info = datetime.datetime(1995, 3, 6, 14, 0, 0)  
today = datetime.datetime(2024, 1, 20)
calculate_biorhythms(today, birth_info, birth_info.time())

import datetime
import random  # Used here for demonstration purposes

def calculate_hormone_levels(date, moon_phase, sun_cycle_phase):
    """
    Simplified calculation of hormone levels based on moon phase and sun cycle phase.
    Note: In a real-world application, these correlations should be based on scientific research.
    """
    # Example hormone levels, these values are placeholders for demonstration
    hormones = {"cortisol": 0, "serotonin": 0, "melatonin": 0}

    # Influence of moon phase on hormone levels
    if moon_phase == "Full Moon":
        hormones["cortisol"] = random.uniform(15, 20)  # Elevated levels
        hormones["melatonin"] = random.uniform(30, 40)  # Decreased levels

    # Influence of sun cycle phase on hormone levels
    if sun_cycle_phase == "Solar Maximum":
        hormones["serotonin"] = random.uniform(70, 80)  # Increased serotonin

    return hormones

# Example usage
date = datetime.datetime.now()
moon_phase = get_moon_phase(date)
sun_cycle_phase = get_sun_cycle_approx(date)
hormone_levels = calculate_hormone_levels(date, moon_phase, sun_cycle_phase)
print(hormone_levels)