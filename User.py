import datetime
import HealthWellnessDashboard

class User:
    def __init__(self, name, birth_datetime):
        self.name = name
        self.birth_datetime = birth_datetime
        self.birth_date = birth_datetime.date()  # Extracting date
        self.birth_time = birth_datetime.time()  # Extracting time

# Usage
user = User("Zachary Confer", datetime.datetime(1995, 5, 1, 7, 0, 0))


# Example usage
user = User("Zachary Confer", datetime.datetime(1995, 3, 6, 7, 0, 0))

dashboard = HealthWellnessDashboard(user)
dashboard.update_dashboard()
dashboard.display_dashboard()
print(dashboard.provide_recommendations())
print(dashboard.track_progress())