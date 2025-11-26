import cv2
import mediapipe as mp
import math

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

mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()
    if not ok:
        continue   

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = face.process(rgb)

    if res.multi_face_landmarks:
        print("face detected")

    cv2.imshow("basic feed", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()