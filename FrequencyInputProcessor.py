class FrequencyInputProcessor:
    def process_auditory_input(self, frequency):
        if frequency < 20:
            return "Infrasound"
        elif frequency <= 20000:
            return "Audible Sound"
        else:
            return "Ultrasound"

    def process_visual_input(self, frequency):
        if 430 <= frequency <= 770:  # THz
            return "Visible Light"
        else:
            return "Invisible Spectrum"

    def process_somatosensory_input(self, frequency):
        # This is a placeholder logic for tactile frequencies
        if frequency < 250:
            return "Fine Texture"
        elif frequency <= 500:
            return "Medium Texture"
        else:
            return "Coarse Texture"
