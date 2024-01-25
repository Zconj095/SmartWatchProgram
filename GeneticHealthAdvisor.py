class GeneticHealthAdvisor:
    def __init__(self, genetic_data):
        self.genetic_data = genetic_data

    def provide_genetic_insights(self):
        # Analyze genetic data for health insights
        risk_factors = "Based on your genetics, you have a higher likelihood of Vitamin D deficiency."
        dietary_advice = "Increase your intake of Vitamin D-rich foods like fatty fish and fortified dairy products."
        return risk_factors, dietary_advice

# Example Usage
user_genetic_data = {"VitaminD_Deficiency_Risk": True}
genetic_advisor = GeneticHealthAdvisor(user_genetic_data)
risk, advice = genetic_advisor.provide_genetic_insights()
print(risk)
print(advice)