import cv2 as cv
# import numpy as np
from object_detection import ObjectDetection
import math


# Initialize Object Detection
obj_det = ObjectDetection()

CLASSES = obj_det.load_class_names()

video = cv.VideoCapture('videos/richard_freethrows.mp4')

curr_frame_count = 0

shot_attempts=0
shot_makes=0

last_made_shot_frame = 0
last_shooting_frame = 0


# Iterates through each frame of video until completion.
# Handles Logic for Displaying and tracking basketball shots
while True:
    ret, frame = video.read()
    curr_frame_count += 1
    if not ret:
        break

    # Score Board
    cv.rectangle(frame, (1525,50), (1875, 250), (0, 0, 0), -1)
    cv.putText(frame, f"Shots Made: {shot_makes}", (1550, 100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255),2)
    cv.putText(frame, f"Shot Attempts: {shot_attempts}", (1550, 150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255),2)
    cv.putText(frame, f"Shooting %:", (1550, 200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255),2)

    if shot_attempts > 0:
        cv.putText(frame, f"{math.trunc((shot_makes/shot_attempts) * 100)}%", (1775, 200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255),2)


    # Detect Objects on frame
    (class_ids, scores, boxes) = obj_det.detect(frame)

    for idx, id in enumerate(class_ids):
        (x,y,w,h) = boxes[idx]
        rounded = math.trunc(scores[idx]*100)

        # if person
        if id == 0:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 10), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 0),2)

        # if backboard
        if id == 1:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (0, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0),2)

        # if net
        if id == 2:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 0, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0),2)

        # if basketball
        if id == 3:
            if scores[idx] > 0.6:
                cv.rectangle(frame, (x,y), (x + w, y+ h), (0, 165, 255), 2)
                cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 165, 255),2)

        # if shooting
        if id == 4:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0),2)
            if curr_frame_count - last_shooting_frame > 30:
                shot_attempts += 1
            last_shooting_frame = curr_frame_count

        # if made basket
        if id == 5:
            cv.rectangle(frame, (x,y), (x + w, y+ h), (255, 255, 0), 2)
            cv.putText(frame, f"{CLASSES[id]} {rounded}%", (x, y - 5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255),2)
            if curr_frame_count - last_made_shot_frame > 60:
                shot_makes += 1
            last_made_shot_frame = curr_frame_count

    cv.imshow("frame", frame)

    key = cv.waitKey(1)
    if key == 27:
        break

video.release()