import cv2
import numpy as np
import base64

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal

from app.schemas.analysis_schema import AnalysisResponse
from app.services.movenet_service import detect_keypoints
from app.services.pose_analysis import calculate_angle
from app.services.excercise_tracker import ExerciseTracker
from app.services.feedback_service import get_feedback

router = APIRouter(prefix="/analysis", tags=["Analysis"])

trackers: dict[str, ExerciseTracker] = {
    "elbow_flexion": ExerciseTracker(),
    "shoulder_raise": ExerciseTracker(),
}

class FrameRequest(BaseModel):
    image: str
    exercise: Literal["elbow_flexion", "shoulder_raise"] = "elbow_flexion"

@router.get("/status")
def status():
    return {"ai_engine": "running", "model": "posenet_tflite"}

@router.post("/reset/{exercise}")
def reset_tracker(exercise: str):
    if exercise in trackers:
        trackers[exercise].reset()
    return {"reset": exercise}

@router.post("/frame", response_model=AnalysisResponse)
def analyze_frame(payload: FrameRequest):
    try:
        img_data = base64.b64decode(payload.image.split(",")[-1])
        np_arr = np.frombuffer(img_data, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        if frame is None:
            raise ValueError
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image data")

    keypoints = detect_keypoints(frame)

    shoulder = keypoints["left_shoulder"]
    elbow    = keypoints["left_elbow"]
    wrist    = keypoints["left_wrist"]

    angle = calculate_angle(shoulder, elbow, wrist)

    tracker = trackers[payload.exercise]
    rep_count = tracker.update(angle, payload.exercise)
    fb = get_feedback(angle, payload.exercise)

    return AnalysisResponse(
        angle=round(angle, 2),
        rep_count=rep_count,
        feedback=fb["feedback"],
        status=fb["status"],
    )
