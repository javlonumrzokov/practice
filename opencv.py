# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     success, frame = cap.read()  # True, False

#     if not success:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     blurred = cv2.GaussianBlur(frame, (15, 15), 0)
#     edges1 = cv2.Canny(frame, 100, 200)
#     edges2 = cv2.Canny(frame, 150, 250)
#     flipped = cv2.flip(frame, 1)

#     cv2.imshow("Original:", frame)
#     # cv2.imshow("Gray:", gray)
#     # cv2.imshow("Blurred:", blurred)
#     # cv2.imshow("edges1:", edges1)
#     # cv2.imshow("edges2:", edges2)
#     cv2.imshow("flipped:", flipped)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    success, frame = cap.read()

    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Real-time face detection:", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
