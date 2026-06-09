import cv2
import numpy as np
import tensorflow as tf
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "posenet.tflite")

interpreter = tf.lite.Interpreter(model_path=MODEL_PATH)
interpreter.allocate_tensors()

_input  = interpreter.get_input_details()[0]
_output = interpreter.get_output_details()[0]

# MoveNet/PoseNet keypoint indices
KEYPOINTS = {
    "nose": 0, "left_eye": 1, "right_eye": 2,
    "left_ear": 3, "right_ear": 4,
    "left_shoulder": 5, "right_shoulder": 6,
    "left_elbow": 7, "right_elbow": 8,
    "left_wrist": 9, "right_wrist": 10,
    "left_hip": 11, "right_hip": 12,
    "left_knee": 13, "right_knee": 14,
    "left_ankle": 15, "right_ankle": 16,
}

def detect_keypoints(frame: np.ndarray) -> dict:
    """Returns {name: [x, y]} for all 17 keypoints. Coordinates are 0-1 normalized."""
    h, w = frame.shape[:2]
    resized = cv2.resize(frame, (257, 257))
    input_data = np.expand_dims(resized.astype(np.float32), axis=0)

    interpreter.set_tensor(_input["index"], input_data)
    interpreter.invoke()

    heatmaps = interpreter.get_tensor(_output["index"])[0]  # (32, 32, 17)

    points = {}
    for name, idx in KEYPOINTS.items():
        heatmap = heatmaps[:, :, idx]
        flat_idx = np.argmax(heatmap)
        gy, gx = divmod(flat_idx, heatmap.shape[1])
        # normalize to 0-1
        points[name] = [gx / heatmap.shape[1], gy / heatmap.shape[0]]

    return points
