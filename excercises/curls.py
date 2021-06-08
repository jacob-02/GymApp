import cv2
from landmark import PoseModule
import time


def curls(n = 0):
    wCam, hCam = 500, 370

    capture = cv2.VideoCapture(n)
    capture.set(3, wCam)
    capture.set(4, hCam)
    pTime = 0

    detector = PoseModule.PoseDetector(detectionCon=0.8)

    while True:
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        frame = detector.findPose(frame)

        lm = detector.findPosition(frame, draw=False)

        if(lm):
            x1, y1 = (lm[24][1], lm[24][2])
            x2, y2 = (lm[23][1], lm[23][2])
            x3, y3 = (lm[26][1], lm[26][2])
            x4, y4 = (lm[25][1], lm[25][2])

            cv2.circle(frame, (x1, y1), 7, (0, 255, 0), cv2.FILLED)

            cv2.circle(frame, (x2, y2), 7, (0, 255, 0), cv2.FILLED)

            cv2.circle(frame, (x3, y3), 7, (0, 255, 0), cv2.FILLED)

            cv2.circle(frame, (x4, y4), 7, (0, 255, 0), cv2.FILLED)

            if (x1 - x3) != 0.0:
                m1 = (y1 - y3) / (x1 - x3)

            if (x2 - x1) != 0.0:
                m = (y2 - y1) / (x2 - x1)
            
            if (x4 - x2) != 0.0:
                m2 = (y4 - y2) / (x4 - x2)

            if (1 + m * m1) != 0.0 or (1 + m * m2) != 0.0:
                alpha = (m1 - m) / (1 + m * m1)
                beta = (m2 - m) / (1 + m * m2)

                print(alpha, beta)


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

curls(1)
