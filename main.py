import cv2
import numpy as np
import time

print("🧙 White Cloak Invisibility Mode!")

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

time.sleep(2)

print("📸 Capturing background... please move out of frame!")
for i in range(30):
    ret, background = cam.read()

background = np.flip(background, axis=1)

cv2.namedWindow("🧙 White Cloak", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(
    "🧙 White Cloak",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)

kernel = np.ones((5, 5), np.uint8)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    frame = np.flip(frame, axis=1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 50, 255])

    mask = cv2.inRange(hsv, lower_white, upper_white)

    # 🔹 MORPHOLOGICAL OPERATIONS
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    mask_inv = cv2.bitwise_not(mask)

    cloak_area = cv2.bitwise_and(background, background, mask=mask)
    non_cloak = cv2.bitwise_and(frame, frame, mask=mask_inv)

    final_output = cv2.addWeighted(cloak_area, 1, non_cloak, 1, 0)

    cv2.imshow("🧙 White Cloak", final_output)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cam.release()
cv2.destroyAllWindows()
