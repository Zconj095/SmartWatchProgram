import numpy as np
import pandas as pd
from scipy.stats import variation

def seasonal_flux_ratio(x, period):
    """
    Calculate seasonal flux ratio for a timeseries with a seasonal period.

    Args:
        x (Pandas Series or NumPy array): Timeseries data 
        period (int): Length of seasonal period  
    Returns:
        float: Seasonal flux ratio
    """
    # Convert to pandas dataframe if necessary
    if isinstance(x, np.ndarray):
        x = pd.DataFrame(x)

    # Group data into seasonal periods 
    grouped_data = x.groupby(x.index // period)
    
    # Calculate coefficient of variation for each period
    fluxes = grouped_data.apply(variation)
    
    # Flux ratio is ratio of max to mean of CVs
    fr = fluxes.max() / fluxes.mean()
    
    return fr

# Example
np.random.seed(123)
index = pd.date_range('2000-01-01', periods=365*5, freq='D')
series = np.random.randn(len(index)) 

fr = seasonal_flux_ratio(series, 365)
print(fr)

# Example
np.random.seed(123)
index = pd.date_range('2000-01-01', periods=365*5, freq='D')
series = np.random.randn(len(index)) 

fr = seasonal_flux_ratio(series, 365)
print(fr)

import numpy as np 
from sklearn.linear_model import LinearRegression
import datetime

# Create sample positional orbit data 
days = 365*5 
dates = [datetime.date(2020, 1, 1) + datetime.timedelta(days=i) for i in range(days)]
orbit = np.sin(np.linspace(0, 4*np.pi, days)) + np.random.normal(0, 0.1, size=days)
orbit = orbit[:,np.newaxis]

# Calculate vertice ranges 
max_orbit = orbit.max(axis=0)
min_orbit = orbit.min(axis=0)
range_orbit = max_orbit - min_orbit
print(f"Orbit range over timeframe: {range_orbit[0]:.3f}")

# Linear regression
model = LinearRegression()
t = np.arange(len(orbit))[:,np.newaxis]
model.fit(t, orbit)
slope = model.coef_[0]  

# Calculate seasonal change
seasonal_change = slope * 365 
print(f"Seasonal orbit change: {seasonal_change[0]:.3f}")


import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Generate sample data
days = 365*5  
t = np.arange(days)
pos_orbit = np.sin(0.01*t) + np.cos(0.03*t)

# Calculate rate of change 
slope, intercept, r_value, p_value, std_err = linregress(t, pos_orbit)
print(f"Rate of change: {slope:.3f} units/day") 

from datetime import datetime
import numpy as np
import pandas as pd
from scipy.stats import linregress

# Set birth date 
birth_date = datetime(1995, 3, 15) # Spring birth

# Create timeframe 
days = (datetime.now() - birth_date).days
dates = [birth_date + pd.Timedelta(days=x) for x in range(days)]

# Create seasonal metric 
np.random.seed(1)
seasons = np.sin(np.linspace(0, 12*np.pi, days)) 

# Biometric measurement
biometrics = seasons + 0.1*np.random.randn(len(dates))

# Rate of change per season 
slopes = []

import numpy as np
import pandas as pd
from scipy.stats import linregress

# Set birth date  
birth_date = datetime(1995, 5, 20)  

# Create daily timeseries  
days = (datetime.now() - birth_date).days + 1
dates = [birth_date + pd.Timedelta(days=x) for x in range(days)]

# Calculate season number 
seasons = [(date.month % 12) // 3 for date in dates]

# Random seasonal impact series
impacts = np.random.randn(len(dates))

# Dataframe to track  
data = pd.DataFrame({"Date": dates, 
                     "Days_since_birth": np.arange(days),
                     "Season": seasons,
                     "Season_Impact": impacts})
                     
# Groupby season  
grouped = data.groupby("Season")

# Print mean daily change per season
print(grouped["Season_Impact"].apply(lambda x: x.diff().mean()))

# Calculate rate of change 
slopes = []
for i in range(len(grouped)):
    x = grouped.get_group(i)["Season_Impact"].values
    y = grouped.get_group(i)["Season_Impact"].diff().values
    slope, _, _, _, _ = linregress(x, y)
    slopes.append(slope)

slope_rate_of_change = linregress(np.arange(len(slopes)), slopes).slope
print(f"Biometric Rate of Seasonal Change: {slope_rate_of_change:.4f}")
from datetime import datetime
import numpy as np
import pandas as pd
from scipy.stats import linregress
import calendar

# Set birth date  
birth_date = datetime(1995, 5, 20)  

# Create daily timeseries  
days = (datetime.now() - birth_date).days + 1
dates = [birth_date + pd.Timedelta(days=x) for x in range(days)]

# Calculate season number 
seasons = [(date.month % 12) // 3 for date in dates]

# Random seasonal impact series
impacts = np.random.randn(len(dates))

# Dataframe to track  
data = pd.DataFrame({"Date": dates, 
                     "Days_since_birth": np.arange(days),
                     "Season": seasons,
                     "Season_Impact": impacts})
                     
# Groupby season  
grouped = data.groupby("Season")

# Print mean daily change per season
print(grouped["Season_Impact"].apply(lambda x: x.diff().mean()))

from datetime import datetime 
import numpy as np
import pandas as pd

# Set birth date  
birth_date = datetime(1995, 5, 20)  

# Create daily timeseries  
days = (datetime.now() - birth_date).days + 1
dates = [birth_date + pd.Timedelta(days=x) for x in range(days)]

# Calculate season number 
seasons = [(date.month % 12) // 3 for date in dates]

# Random seasonal impact series
impacts = np.random.randn(len(dates))

# Dataframe to track  
data = pd.DataFrame({"Date": dates, 
                     "Days_since_birth": np.arange(days),
                     "Season": seasons,
                     "Season_Impact": impacts})
                     
# Groupby season  
grouped = data.groupby("Season")

# Print mean daily change per season
print(grouped["Season_Impact"].apply(lambda x: x.diff().mean()))

from datetime import datetime
import ephem
import pandas as pd
import numpy as np
from scipy.signal import periodogram

# Birth details
birth_date = datetime(1995, 3, 15)
birth_season = (birth_date.month%12)//3 
birth_moon = ephem.next_full_moon(birth_date)
birth_solar = "Solar_Max" # example

# Current details  
today = datetime.now()
today_season = (today.month%12)//3
today_moon = ephem.next_full_moon(today) 
today_solar = "Solar_Min"

import numpy as np

# Set orbital parameters
orbit_period = 365 # days 
season_lengths = [90, 92, 93, 90] 
axis_tilt = 23.5 # degrees

# Initialize variables
time = np.arange(orbit_period)
insolation = np.zeros(orbit_period)
temp = 10  

# Calculate insolation based on tilt
for t in time:
    theta = (t / orbit_period) * 2*np.pi 
    axis_dir = np.cos(theta) * axis_tilt
    insolation[t] = np.cos(axis_dir)
    
# Seasonal temp calculation   
temps = []
for i in range(len(season_lengths)):
    season_insolation = insolation[i*90:(i+1)*90] 
    season_temp = temp + np.mean(season_insolation) - 0.5
    temp = season_temp
    temps.append(season_temp)
    
precipitation = 0
for i in range(len(season_lengths)):
    season_temp = temps[i]
    season_precip = precipitation + np.random.randn()*season_temp 
    precipitation = season_precip
    
# Calculate biorhythm
days = len(insolation)
biorhythm = np.sin(2*np.pi*np.arange(days)/23)


# Frequency analysis
freq_birth, power_birth = periodogram(biorhythm[:len(biorhythm)//2])
freq_today, power_today = periodogram(biorhythm[len(biorhythm)//2:])

# Calculate flux change 
flux_change = (power_today.max() - power_birth.max()) / power_birth.max()  

# Print analysis
print(f"Season Change: {birth_season} to {today_season}") 
print(f"Moon Phase Shift: {birth_moon} to {today_moon}")
print(f"Solar Change: {birth_solar} to {today_solar}")
print(f"Biorhythm Frequency Flux: {flux_change:.3f}")

import numpy as np
import matplotlib.pyplot as plt

# Season parameters
season_lengths = [90, 92, 93, 90] # lengths of each season  
season_names = ['Winter','Spring','Summer','Autumn']
wait_times = [14, 10, 16, 12] # wait times between seasons

# Simulation timesteps   
timestep = 0.1
timesteps_per_season = [int(l/timestep) for l in season_lengths]

# Climate variable to track
temp = 10 

# Initialization
time_points = []
temp_values = []

# Run simulation 
for i in range(len(season_lengths)):
    
    # Simulate season   
    for t in range(timesteps_per_season[i]):
        temp_diff = 0.1*(t/timesteps_per_season[i] - 0.5)  
        temp += temp_diff  
        time_points.append(timestep*t)
        temp_values.append(temp)

    # Wait time     
    for t in range(int(wait_times[i]/timestep)):
        time_points.append(time_points[-1] + timestep) 
        temp_values.append(temp_values[-1])

import numpy as np
import matplotlib.pyplot as plt

# Set orbital parameters
orbit_period = 365 # days 
season_lengths = [90, 92, 93, 90] 
axis_tilt = 23.5 # degrees

# Initialize variables
time = np.arange(orbit_period)
insolation = np.zeros(orbit_period)
temp = 10  

# Calculate insolation based on tilt
for t in time:
    theta = (t / orbit_period) * 2*np.pi 
    axis_dir = np.cos(theta) * axis_tilt
    insolation[t] = np.cos(axis_dir)
    
# Seasonal temp calculation   
temps = []
for i in range(len(season_lengths)):
    season_insolation = insolation[i*90:(i+1)*90] 
    season_temp = temp + np.mean(season_insolation) - 0.5
    temp = season_temp
    temps.append(season_temp)
    