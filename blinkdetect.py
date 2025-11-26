import cv2
import mediapipe as mp
import math
import time

mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh()

L_EYE = [33,160,158,133,153,144]
R_EYE = [362,387,385,263,380,373]

def ear_calc(idx, marks):
    try:
        A = math.dist(marks[idx[1]], marks[idx[5]])
        B = math.dist(marks[idx[2]], marks[idx[4]])
        C = math.dist(marks[idx[0]], marks[idx[3]])
        return (A + B) / (2 * C)
    except:
        return 0

THRESH = 0.27

blink_start = None
blink_count = 0
last_blink_time = 0

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = face.process(rgb)
    now = time.time()

    if res.multi_face_landmarks:
        h, w, _ = frame.shape
        for lm in res.multi_face_landmarks:
            pts = [(int(p.x*w), int(p.y*h)) for p in lm.landmark]
            ear = (ear_calc(L_EYE, pts) + ear_calc(R_EYE, pts)) / 2

            if ear < THRESH:
                if blink_start is None:
                    blink_start = now
            else:
                if blink_start is not None:
                    dur = now - blink_start

                    if now - last_blink_time < 0.35:
                        blink_count += 1
                    else:
                        blink_count = 1

                    print("blinks:", blink_count)
                    last_blink_time = now
                    blink_start = None

    cv2.imshow("multi blink test", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()