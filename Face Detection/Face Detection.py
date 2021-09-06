import cv2

haar_cascade = "haarcascade_frontalface.xml"
detector = cv2.CascadeClassifier(haar_cascade)

vc = cv2.VideoCapture(0)

while(True):
    
    _, frame = vc.read()
    grayScaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    coordinates = detector.detectMultiScale(grayScaleFrame, 1.3, 4)
    for (x, y, w, h) in coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    cv2.imshow("Face Detector", frame)
    if ord('q') == cv2.waitKey(1) & 0xFF:
        break
    
vc.release()
cv2.destroyAllWindows()