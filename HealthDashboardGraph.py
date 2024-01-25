import HealthDashboard
import CentralHealthSystem
import matplotlib.pyplot as plt
class HealthDashboard:
    def __init__(self, user_health_data):
        self.user_health_data = user_health_data

    def display(self):
        # Existing logic to display the health dashboard
        pass

    def display_graph(self, data_type):
        # Logic to display a graph
        if data_type in self.user_health_data and self.user_health_data[data_type] is not None:
            data = self.user_health_data[data_type]
            dates = list(data.keys())
            values = list(data.values())

            plt.figure(figsize=(10, 5))
            plt.plot(dates, values, marker='o')
            plt.title(f"{data_type} Over Time")
            plt.xlabel("Date")
            plt.ylabel("Value")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print(f"No data available for {data_type}")

# Example usage
user_health_data = {
    'Wearable Data': {
        '2021-01-01': 10000,
        '2021-01-02': 10500,
        '2021-01-03': 9800,
        # ... more data ...
    }
}

# Ensure the instance of HealthDashboard is created after the class is defined with the display_graph method
central_system.health_dashboard = HealthDashboard(user_health_data)
central_system = CentralHealthSystem(user_profile, nutritional_data, wearable_device)
central_system.update_system()
central_system.health_dashboard.display_graph('Wearable Data')
