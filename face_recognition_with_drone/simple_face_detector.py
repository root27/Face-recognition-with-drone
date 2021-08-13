import cv2

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True:
    img, frame = cap.read() 
    gray_scaledimage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(gray_scaledimage)
    
    for (x, y, w, h) in face_coordinates:
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    
    
    cv2.imshow('Frame', frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
