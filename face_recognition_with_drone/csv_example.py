
import xlwt
import KeyPressModule as kp
import cv2
import time
import datetime
from djitellopy import Tello

from time import sleep

kp.init()
drone = Tello()
drone.connect()
print(drone.get_battery())


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 60
    

    if kp.getKey('q'): lr = -speed
    elif kp.getKey('r'): lr = speed
    
    if kp.getKey('e'): ud = speed
    elif kp.getKey('f'): ud = -speed
    
    if kp.getKey('w'): fb = speed
    elif kp.getKey('s'): fb = -speed
    
    if kp.getKey('a'): yv = -speed
    elif kp.getKey('d'): yv = speed
    
    if kp.getKey('z'): 
        drone.streamoff()
        drone.land()
        
    return [lr, fb, ud, yv]

i = 0
drone.takeoff()
drone.streamon()
frame_read = drone.get_frame_read()
book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet("Sheet 1")
while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sheet1.write(i, 1, vals[0])
    sheet1.write(i, 2, vals[1])
    sheet1.write(i, 3, vals[2])
    sheet1.write(i, 4, vals[3])
    frame = frame_read.frame
    date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
    img_name = date + ".jpg"
    cv2.imwrite(img_name, frame)
        #f = open("driving_log.csv", "a+")
    sheet1.write(i, 0, img_name)
    i=i+1
    time.sleep(0.5)
    if kp.getKey('c'):
        break
    #cv2.imshow('Drone', frame)
    #key = cv2.waitKey(1) & 0xff  

book.save("driving_log.csv")


    
    