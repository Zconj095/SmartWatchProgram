class HealthAnomalyDetection:
    def __init__(self, user_health_data):
        self.user_health_data = user_health_data

    def detect_anomalies(self):
        # Placeholder for anomaly detection logic
        if self.user_health_data['heart_rate'] > 100:
            return "Anomaly detected: Elevated heart rate. Consider consulting a physician if this persists."
        return "No anomalies detected in recent health data."

# Example Usage
user_health_data = {'heart_rate': 102, 'activity_level': 'low'}
anomaly_detection = HealthAnomalyDetection(user_health_data)
print(anomaly_detection.detect_anomalies())