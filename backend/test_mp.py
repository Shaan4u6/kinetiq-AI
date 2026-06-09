import mediapipe as mp

print("Version:", mp.__version__)
print("Has solutions:", hasattr(mp, "solutions"))

if hasattr(mp, "solutions"):
    print("SUCCESS")
    print(mp.solutions.pose)