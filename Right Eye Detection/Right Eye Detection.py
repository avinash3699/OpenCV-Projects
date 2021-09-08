import cv2

rightEyeCascade = cv2.CascadeClassifier("haarcascade_righteye_2splits.xml")

vc = cv2.VideoCapture(0)

while(True):
    
    _, frame = vc.read()
    
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    coordinates = rightEyeCascade.detectMultiScale(grayImage, 1.3, 4)
    for (x, y, w, h) in coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        
    cv2.imshow("Right Eye Detection", frame)
    
    # press esc to break the loop
    if cv2.waitKey(1) == 27:
        break
    
vc.release()
cv2.destroyAllWindows()
