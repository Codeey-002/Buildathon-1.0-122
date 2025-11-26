import cv2
import mediapipe as mp
import math

mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh()

L_EYE = [33,160,158,133,153,144]
R_EYE = [362,387,385,263,380,373]

def eye_ar(eye_idx, marks):
    try:
        A = math.dist(marks[eye_idx[1]], marks[eye_idx[5]])
        B = math.dist(marks[eye_idx[2]], marks[eye_idx[4]])
        C = math.dist(marks[eye_idx[0]], marks[eye_idx[3]])
        return (A + B) / (2 * C)
    except:
        return 0

THRESH = 0.25  

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        continue

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = face.process(rgb)

    if res.multi_face_landmarks:
        h, w, _ = frame.shape
        for lm in res.multi_face_landmarks:
            points = [(int(p.x*w), int(p.y*h)) for p in lm.landmark]

            l = eye_ar(L_EYE, points)
            r = eye_ar(R_EYE, points)
            ear = (l + r) / 2

            print("EAR:", round(ear,3))

    cv2.imshow("EAR debug", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()