class ExerciseTracker:
    def __init__(self):
        self.counter = 0
        self.stage = None

    def update(self, angle: float, exercise: str = "elbow_flexion") -> int:
        if exercise == "elbow_flexion":
            if angle < 40:
                self.stage = "down"
            if angle > 140 and self.stage == "down":
                self.stage = "up"
                self.counter += 1

        elif exercise == "shoulder_raise":
            if angle < 30:
                self.stage = "down"
            if angle > 80 and self.stage == "down":
                self.stage = "up"
                self.counter += 1

        return self.counter

    def reset(self):
        self.counter = 0
        self.stage = None
