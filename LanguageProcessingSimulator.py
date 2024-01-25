class LanguageProcessingSimulator:
    def __init__(self, linguistic_exposure, emotional_responses):
        self.linguistic_exposure = linguistic_exposure
        self.emotional_responses = emotional_responses
        self.belief_changes = {}

    def process_linguistic_exposure(self):
        for word, exposure in self.linguistic_exposure.items():
            if exposure['frequency'] > 5:  # Threshold for belief change
                self.belief_changes[word] = 'belief strengthened'
            elif exposure['novelty'] > 7:  # Scale of 1 to 10
                self.belief_changes[word] = 'new belief formed'

    def process_emotional_response_to_language(self):
        for word, emotion in self.emotional_responses.items():
            if emotion in ['joy', 'surprise']:
                self.belief_changes[word] = 'positive belief association'
            elif emotion in ['fear', 'sadness']:
                self.belief_changes[word] = 'negative belief association'

    def get_belief_changes(self):
        return self.belief_changes

linguistic_exposure = {
    "empathy": {"frequency": 6, "novelty": 5},
    "ganbatte": {"frequency": 3, "novelty": 8}
}

emotional_responses = {
    "empathy": "joy",
    "ganbatte": "surprise"
}

language_processor = LanguageProcessingSimulator(linguistic_exposure, emotional_responses)
language_processor.process_linguistic_exposure()
language_processor.process_emotional_response_to_language()
belief_changes = language_processor.get_belief_changes()

print("Belief Changes due to Language Exposure and Emotional Response:", belief_changes)
