#computer vision = cv
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow("Ouptput", frame)
    if cv2.waitKey(16)  == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()