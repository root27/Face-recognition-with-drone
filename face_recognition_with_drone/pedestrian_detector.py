import cv2

pedestrian_tracker = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

webcam = cv2.VideoCapture(0)

while True:
    img, frame = webcam.read()
    
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    pedestrians = pedestrian_tracker.detectMultiScale(grayscale_image)
    
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) 
        
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
