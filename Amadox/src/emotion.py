import cv2
from deepface import DeepFace
from transformers import pipeline


class EmotionEngine:
    """
    Core AI logic for Feature 1 (Real-Time Detection) and
    Feature 4 (Stress Management).
    """

    def __init__(self):
        # Feature 1: Load pre-trained NLP model for text emotion analysis
        self.text_analyzer = pipeline("text-classification",
                                      model="j-hartmann/emotion-english-distilroberta-base")
        # Feature 4: Stress tracking variables
        self.stress_counter = 0
        self.STRESS_THRESHOLD = 30  # Number of continuous negative frames before alert

    def detect_facial_emotion(self, frame):
        """
        Analyzes live camera video frames for emotions.
        """
        try:
            # DeepFace analyze handles Feature 1's comprehensive detection
            results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            return results[0]['dominant_emotion']
        except Exception as e:
            return "neutral"

    def detect_text_emotion(self, text_input):
        """
        Analyzes employee text inputs for sentiment.
        """
        if not text_input:
            return "neutral"
        result = self.text_analyzer(text_input)
        return result[0]['label']

    def check_for_stress_alert(self, current_emotion):
        """
        Feature 4: Automatically identifies prolonged stress or burnout.
        """
        # Emotions typically associated with workplace stress
        negative_emotions = ["angry", "sad", "fear", "disgust"]

        if current_emotion in negative_emotions:
            self.stress_counter += 1
        else:
            self.stress_counter = max(0, self.stress_counter - 1)

        # Trigger alert if negative mood is prolonged
        if self.stress_counter >= self.STRESS_THRESHOLD:
            return True  # Signal to main app to notify HR at support@amdox.in
        return False