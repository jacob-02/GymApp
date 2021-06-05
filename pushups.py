import cv2
from landmark import PoseModule
import time

wCam, hCam = 1000, 700

capture = cv2.VideoCapture(0)
capture.set(3, wCam)
capture.set(4, hCam)
pTime = 0
volume = 20.0
volumeList = []
muter = 20.0

detector = PoseModule.PoseDetector(detectionCon=0.8)

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame = detector.findPose(frame)

    lm = detector.findPosition(frame, draw=False)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)) + " fps", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()