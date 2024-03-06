import cv2 as cv
# import numpy as np
from object_detection import ObjectDetection
import math

# Initialize Object Detection
objdet = ObjectDetection()

cap = cv.VideoCapture('videos/richard_freethrows.mp4')

#initialize count
count = 0
prev_center_points = []

tracking_objs = {}
track_id = 0



while True:

    ret, frame = cap.read()
    count += 1
    if not ret:
        break

    #Point current frame
    curr_center_points = []

    #Detect Objects on Frame
    (class_ids, scores, boxes) = objdet.detect(frame)
    for box in boxes:
        (x,y,w,h) = box
        cx = int((x + x + w)/2)
        cy = int((y + y + h)/2)
        curr_center_points.append((cx,cy))
        print('FRAME Num ', count,"", x,y,w,h)
        cv.rectangle(frame, (x,y),(x+w, y+h),(0, 255, 0), 2)

    if count < 3:
        for pt in curr_center_points:
            for pt2 in prev_center_points:
                distance = math.hypot(pt2[0] - pt[0], pt2[1]-pt[1])

                if distance < 10:
                    tracking_objs[track_id] = pt
                    track_id += 1

    else:
        tracking_objs_copy = tracking_objs.copy()
        curr_center_points_copy = curr_center_points.copy()

        for object_id, pt2 in tracking_objs_copy.items():

            object_exists = False
            for pt in curr_center_points:
                distance = math.hypot(pt2[0] - pt[0], pt2[1]-pt[1])


                # update id position

                if distance < 20:
                    tracking_objs[object_id] = pt
                    object_exists = True
                    if pt in curr_center_points:
                        curr_center_points.remove(pt)
                    continue
            #remove id
            if not object_exists:
                tracking_objs.pop(object_id)

        #add new ids found
        for pt in curr_center_points:
            tracking_objs[track_id] = pt
            track_id += 1

    for object_id, pt in tracking_objs.items():
        cv.circle(frame, pt, 5, (0,0,255), -1)
        cv.putText(frame, str(object_id),(pt[0],pt[1]- 7), 0,1,(0,0,255),2)

    print('tracking objects', tracking_objs)


    print('Curr frame')
    print(curr_center_points)

    print('prev frame')
    print(prev_center_points)

    cv.imshow('Frame', frame)

    #make a copy of points
    prev_center_points = curr_center_points.copy()

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()