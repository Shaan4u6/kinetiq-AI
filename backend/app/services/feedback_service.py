def get_feedback(angle: float, exercise: str = "elbow_flexion") -> dict:
    if exercise == "elbow_flexion":
        if angle < 40:
            return {"status": "incorrect", "feedback": "Bend your elbow more"}
        if angle > 160:
            return {"status": "incorrect", "feedback": "Extend arm fully then curl"}
        return {"status": "correct", "feedback": "Good elbow flexion"}

    if exercise == "shoulder_raise":
        if angle < 60:
            return {"status": "incorrect", "feedback": "Raise your arm higher"}
        if angle > 120:
            return {"status": "incorrect", "feedback": "Lower your arm slightly"}
        return {"status": "correct", "feedback": "Good shoulder raise"}

    return {"status": "correct", "feedback": "Pose detected"}
