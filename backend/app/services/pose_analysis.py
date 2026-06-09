import math

def calculate_angle(a: list, b: list, c: list) -> float:
    """Calculate angle at point b given three [x, y] points."""
    angle = abs(
        math.degrees(
            math.atan2(c[1] - b[1], c[0] - b[0]) -
            math.atan2(a[1] - b[1], a[0] - b[0])
        )
    )
    return 360 - angle if angle > 180 else angle
