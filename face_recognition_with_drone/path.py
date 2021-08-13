from tensorflow.keras.preprocessing.image import img_to_array
import tensorflow as tf
from imutils.video import VideoStream
from threading import Thread
import numpy as np
import imutils
import time
from tello import Tello
import argparse
import utils
import cv2
import os

left_right_velocity = 0
forward_backward_velocity = 0
up_down_velocity = 0
yaw_velocity = 0

drone = Tello()


MODEL_PATH = "example.model"

print("[INFO] loading model...")
model = tf.keras.models.load_model(MODEL_PATH)

drone.connect()
time.sleep(0.5)
drone.streamon()


print("[INFO] starting video stream...")

drone.takeoff()

while True:
    frame_read = drone.get_frame_read()
    img = frame_read.frame
    frame = imutils.resize(img, width=400)
    
    image = utils.preprocess(img)
    
    #image = image.astype("float") / 255.0
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    
    steering_angle = float(model.predict(image, batch_size=1))
    if steering_angle < 0:
        #label = "straight"
        print("Turning left")
        drone.rotate_counter_clockwise(-steering_angle)
        drone.send_rc_control(0, 30, 0, 0) 
    elif steering_angle > 0:
        #label = "turnleft"
        print("Turning right")
        drone.rotate_clockwise(steering_angle)
        drone.send_rc_control(0, 30, 0, 0)
        
    else:
        #label = "turnright"
        print("Going straight")
        drone.send_rc_control(0, 30, 0, 0)
        
                              
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break

print("[INFO] cleaning up...")
cv2.destroyAllWindows()
drone.land()
