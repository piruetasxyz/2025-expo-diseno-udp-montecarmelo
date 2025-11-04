import vlc
import os
import cv2

# Video file paths
video1_path = "data/085.mp4"
video2_path = "data/097.mp4"

# Open video captures
cap1 = cv2.VideoCapture(video1_path)
cap2 = cv2.VideoCapture(video2_path)

# Create named windows
cv2.namedWindow("Monitor 1 Video")
cv2.namedWindow("Monitor 2 Video")

# Position windows (adjust coordinates based on your monitor setup)
# Assuming Monitor 1 is to the left of Monitor 2
# Top-left of Monitor 1
cv2.moveWindow("Monitor 1 Video", 0, 0)
# Top-left of Monitor 2 (if Monitor 1 is 1920px wide)
cv2.moveWindow("Monitor 2 Video", 1920, 0)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print("pucha no hay ret1 o ret2")

    cv2.imshow("Monitor 1 Video", frame1)
    cv2.imshow("Monitor 2 Video", frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("pucha se presiono q")

cap1.release()
cap2.release()
cv2.destroyAllWindows()
