import cv2
import numpy as np

class PoseDetector:

    def detect(self, frame):
        height, width, _ = frame.shape

        return {
            "left_shoulder": [width * 0.4, height * 0.3],
            "left_elbow":    [width * 0.45, height * 0.45],
            "left_wrist":    [width * 0.5, height * 0.6]
        }
