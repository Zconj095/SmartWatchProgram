class HealthDashboard:
    def __init__(self, user_health_data):
        self.user_health_data = user_health_data

    def display(self):
        print("Health and Wellness Dashboard")
        for metric, value in self.user_health_data.items():
            print(f"{metric}: {value}")
        pass    
    
    def display2(self):
        print("Health and Wellness Dashboard")
        for metric, value in self.user_health_data.items():
            if isinstance(value, dict):
                for sub_metric, sub_value in value.items():
                    print(f"{sub_metric}: {sub_value}")
            else:
                print(f"{metric}: {value}")

