import cv2
import numpy as np
import os

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False, varThreshold=145, history=700)
fgbg.setNMixtures(3)

roi = []
def get_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Clicked at coordinates (", x, ", ", y, ")")
        if len(roi) < 2:
            roi.append([x,y])


cv2.namedWindow("video")

cv2.setMouseCallback("video", get_coords)

grid_size = 50
color = (0,255,0)
thickness = 1

dirname = 'C:\\Personal Drive\\Movement_Detector\\OpenCV_MOG2\\color'
os.chdir(dirname)

for files in os.listdir(dirname):
    frame = cv2.imread(files)
    fgmask = fgbg.apply(frame)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    fg_mask = cv2.erode(fgmask, kernel) 
    fg_mask = cv2.dilate(fg_mask, kernel)

    for i in range(0, frame.shape[1], grid_size):
        cv2.rectangle(frame, (i, 0), (i+grid_size, frame.shape[0]), color, thickness)   
    for j in range(0, frame.shape[0], grid_size):
        cv2.rectangle(frame, (0, j), (frame.shape[1], j+grid_size), color, thickness)
    
    if len(roi) < 2:
        cv2.imshow("fg_mask", fg_mask)
    elif len(roi) == 2:
        num_white_pixels = cv2.countNonZero(fg_mask)
        contours, hierarchy = cv2.findContours(fg_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
        if num_white_pixels > 1700:
            cv2.putText(frame, "MOTION DETECTED", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        else:
            cv2.putText(frame, "NO MOTION DETECTED", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
        cv2.imshow("fg_mask", fg_mask[roi[0][1]:roi[1][1], roi[0][0]:roi[1][0]])
    
    cv2.imshow("video", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break 

cv2.destroyAllWindows() 
