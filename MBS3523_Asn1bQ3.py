import cv2

print(cv2.__version__)

x, y = 80, 40
dx, dy = 9, 4

capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

while True:
    success, frame = capture.read()

    cv2.putText(frame, 'MBS3523 Assignment 1b – Q3 Name: Ho Yat Long', (20, 40), cv2. FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    cv2.rectangle(frame, (x, y), (x + 80, y + 80), (255, 0, 0), 2)

    y += dy
    x += dx

    if y >= 400 or y <= 0:
       dy *= -1
    if x >= 560 or x <= 0:
           dx *= -1

    cv2.imshow('MBS3523', frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()