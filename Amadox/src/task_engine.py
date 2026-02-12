def get_recommendation(emotion):
    """Suggests tasks based on the detected mood (Feature 2)."""
    mapping = {
        "happy": "Creative Brainstorming or Client Meetings",
        "neutral": "Deep Work: Coding, Writing, or Analysis",
        "sad": "Administrative work or Light Data Entry",
        "angry": "Independent Technical Tasks or Research",
        "fear": "Team Sync or Mentorship Check-in",
        "surprise": "New Feature Design or Strategy Review",
        "disgust": "Organization: Document Filing or Inbox Zero"
    }
    return mapping.get(emotion, "Routine daily schedule")