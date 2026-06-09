import cv2

from app.services.mediapipe_service import detect_pose

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    results = detect_pose(frame)

    if results.pose_landmarks:

        print("Body Detected")

    cv2.imshow(
        "Pose Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()