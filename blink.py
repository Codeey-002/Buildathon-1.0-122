import cv2
import mediapipe as mp

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