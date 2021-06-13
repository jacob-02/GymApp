from os import altsep
import cv2
from landmark import PoseModule
import time
import math


def curls(n = 0):
    wCam, hCam = 500, 370

    capture = cv2.VideoCapture(n)
    capture.set(3, wCam)
    capture.set(4, hCam)
    pTime = 0
    count = 0

    detector = PoseModule.PoseDetector(detectionCon=0.8)

    while True:
        ret, frame = capture.read()

        if not ret:
            capture.release()
            cv2.destroyAllWindows()
            break

        frame = cv2.flip(frame, 1)
        frame = detector.findPose(frame)

        lm = detector.findPosition(frame, draw=False)

        if(lm):
            x1, y1 = (lm[12][1], lm[12][2])
            x3, y3 = (lm[11][1], lm[11][2])
            x2, y2 = (lm[16][1], lm[16][2])
            x4, y4 = (lm[15][1], lm[15][2])

            cv2.circle(frame, (x1, y1), 7, (0, 255, 0), cv2.FILLED)
            cv2.circle(frame, (x2, y2), 7, (0, 255, 0), cv2.FILLED)
            cv2.circle(frame, (x3, y3), 7, (0, 255, 0), cv2.FILLED)
            cv2.circle(frame, (x4, y4), 7, (0, 255, 0), cv2.FILLED)
            
            alpha = math.hypot((y4 - y3), (x4 - x3))
            beta = math.hypot((y1 - y2), (x1 - x2))

            if(alpha <= 50.0):
                n = 0

            if(beta >= 100.0 and n == 0):
                n = 1
                count += 1
            
            cv2.putText(frame, str(count), (250, 300), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=2, color=(0, 255, 0), thickness=2)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(frame, str(int(fps)) + " fps", (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

        cv2.imshow('Webcam', frame)

        if cv2.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()
    cv2.destroyAllWindows()
    