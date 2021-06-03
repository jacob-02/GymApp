import mediapipe as mp
import cv2
import time

class PoseDetector:
    def __init__(self, mode=False, max_pose=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.max_pose = max_pose
        self.trackCon = trackCon
        self.detectionCon = detectionCon
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.max_pose, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.detectedPose = False

    def findPose(self, frame, draw=True):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(image)

        if self.results.pose_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(frame, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS,
                                               self.mpDraw.DrawingSpec(color=(0, 0, 0), thickness=2, circle_radius=2),
                                               self.mpDraw.DrawingSpec(color=(155, 155, 155), thickness=2,
                                                                       circle_radius=2))
        return frame

    def findPosition(self, frame, poseNo=0, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            poseLms = self.results.pose_landmarks
            self.detectedPose = True
            for id, lm in enumerate(poseLms.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(frame, (cx, cy), 5, (0, 0, 0), cv2.FILLED)

        else:
            self.detectedPose = False

        return lmList


wCam, hCam = 700, 500

capture = cv2.VideoCapture(0)
capture.set(3, wCam)
capture.set(4, hCam)
pTime = 0
volume = 20.0
volumeList = []
muter = 20.0

detector = PoseDetector(detectionCon=0.8)

while True:
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    frame = detector.findPose(frame)

    lm = detector.findPosition(frame, draw=False)

    distance = 0

    if len(lm) != 0:
        x1, y1 = lm[11][1], lm[11][2]
        x2, y2 = lm[12][1], lm[12][2]

        cv2.circle(frame, (x1, y1), 10, (0, 255, 0), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 10, (0, 255, 0), cv2.FILLED)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(frame, str(int(fps)) + " fps", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)

    cv2.imshow('Webcam', frame)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
