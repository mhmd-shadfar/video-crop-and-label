import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_with_box = cv2.rectangle(gray, (100, 100), (50, 50), (255, 255, 255), 5)

    cv2.imshow('frame', gray_with_box)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
