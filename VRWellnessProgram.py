class VRWellnessProgram:
    def start_session(self, program_type, user_preferences):
        print(f"Initiating {program_type} session with settings: {user_preferences}")

    def adjust_session_settings(self, adjustments):
        print(f"Session settings adjusted: {adjustments}")
        
vr_wellness = VRWellnessProgram()
vr_wellness.start_session('Meditation', {'environment': 'Forest', 'duration': '20 minutes'})
vr_wellness.adjust_session_settings({'environment': 'Beach'})