import cv2
from deepface import DeepFace
from task_engine import get_recommendation
from tracker import log_mood, get_team_analytics


def run_system():
    cap = cv2.VideoCapture(0)
    stress_streak = 0
    print("Amdox AI Task Optimizer is Live...")

    while True:
        ret, frame = cap.read()
        if not ret: break

        try:
            # Feature 1: Real-Time Facial Emotion Detection
            res = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            mood = res[0]['dominant_emotion']

            # Feature 3: Historical Tracking
            log_mood(mood)

            # Feature 2: Task Recommendation
            task = get_recommendation(mood)

            # Feature 4: Stress Alerts (Trigger after 50 frames of negative mood)
            if mood in ["angry", "sad", "fear"]:
                stress_streak += 1
            else:
                stress_streak = 0

            # UI Display
            cv2.putText(frame, f"Mood: {mood}", (20, 40), 1, 1.5, (0, 255, 0), 2)
            cv2.putText(frame, f"Task: {task}", (20, 80), 1, 1.2, (255, 255, 255), 1)

            if stress_streak > 50:
                cv2.putText(frame, "STRESS ALERT: Contacting HR", (20, 120), 1, 1.2, (0, 0, 255), 2)

        except:
            pass

        cv2.imshow('Amdox AI Optimizer', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Team Analytics Summary (Feature 5):", get_team_analytics())
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_system()