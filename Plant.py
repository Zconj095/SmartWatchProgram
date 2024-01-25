class Plant:
    
    def __init__(self, season_cycle): 
        self.season_cycle = season_cycle
        self.phase = 0
        
    def update(self, season):
        if self.phase < len(self.season_cycle) and season == self.season_cycle[self.phase]:
            self.phase += 1 

# Example sugar maple
sugar_maple = Plant([0, 1, 2])

population = 1000 

activities = {
    "PlantCrops": [1, 2], 
    "HarvestCrops": [3],
    "Hunt": [0, 3],
    "StayInside": [2]
}

activity = np.random.choice(list(activities.keys()), p=[0.3, 0.3, 0.2, 0.2])
