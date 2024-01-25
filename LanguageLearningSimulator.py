class LanguageLearningSimulator:
    def __init__(self, new_concepts, cultural_concepts):
        self.new_concepts = new_concepts
        self.cultural_concepts = cultural_concepts

    def introduce_new_concepts(self, language):
        return self.new_concepts.get(language, "No new concepts for this language")

    def introduce_cultural_concepts(self, language):
        return self.cultural_concepts.get(language, "No cultural concepts for this language")

new_concepts = {
    "Spanish": ["empatia (empathy)", "amistad (friendship)"],
    "Japanese": ["kizuna (bond)", "ganbatte (perseverance)"]
}

cultural_concepts = {
    "Chinese": ["feng shui", "yin and yang"],
    "French": ["joie de vivre", "terroir"]
}

language_simulator = LanguageLearningSimulator(new_concepts, cultural_concepts)
spanish_concepts = language_simulator.introduce_new_concepts("Spanish")
chinese_culture = language_simulator.introduce_cultural_concepts("Chinese")

print("New Concepts in Spanish:", spanish_concepts)
print("Cultural Concepts in Chinese:", chinese_culture)
