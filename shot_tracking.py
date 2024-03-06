import cv2 as cv
# import numpy as np
from object_detection import ObjectDetection
import math


# Initialize Object Detection
obj_det = ObjectDetection()

CLASSES = obj_det.load_class_names()
print(CLASSES)

video = cv.VideoCapture('videos/richard_freethrows.mp4')



frame_count = 0


'''
0 = person
1 = backboard
2 = net
3 = basketball
4 = shooting
5 = made basket
'''
while True:
    ret, frame = video.read()
    frame_count += 1
    if not ret:
        break


    # Detect Objects on frame
    (class_ids, scores, boxes) = obj_det.detect(frame)
    print("scores", scores)
    print("class ids", class_ids)
    for idx, id in enumerate(class_ids):
        (x,y,w,h) = boxes[idx]
        rounded = math.trunc(scores[idx]*100)

        # if person
        if id == 0:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 10), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 0),2)

        # if backboard
        if id == 1:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0),2)

        # if net
        if id == 2:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (0, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0),2)

        # if basketball
        if id == 3:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 165, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 165, 0),2)

        # if shooting
        if id == 4:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0),2)

        # if made basket
        if id == 5:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0),2)

    cv.imshow("frame", frame)

    key = cv.waitKey(0)
    if key == 27:
        break

video.release()