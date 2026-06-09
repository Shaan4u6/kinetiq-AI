import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose

pose_detector = mp_pose.Pose(
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def detect_pose(frame):

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    results = pose_detector.process(rgb_frame)

    return results