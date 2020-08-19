from cv2 import cv2

img_file = 'cari.jpg'

car_file = 'car_detector.xml'
pedestrian_file = 'pedestrian.xml'

video = cv2.VideoCapture('bike.mp4')

pedestrian_tracker = cv2.CascadeClassifier(pedestrian_file)
car_tracker = cv2.CascadeClassifier(car_file)

while True:
    (read_successful,frame) = video.read()
    if read_successful:
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    else:
        break
    
    cars = car_tracker.detectMultiScale(gray_frame)
    pedestrian = pedestrian_tracker.detectMultiScale(gray_frame)

    for(x,y,w,h) in cars:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), (2))
    
    for(x,y,w,h) in pedestrian:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), (2))


    cv2.imshow('win',frame)
    cv2.waitKey(1)


print('ho')