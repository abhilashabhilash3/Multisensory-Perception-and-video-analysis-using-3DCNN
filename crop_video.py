import numpy as np
import cv2

cap = cv2.VideoCapture('MO_New_Video.mp4')

cnt = 0

w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

x,y,h,w = 400,400,400,1100

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('MO_New_Video_cropped.mp4', fourcc, fps, (w, h))

while(cap.isOpened()):
    ret, frame = cap.read()

    cnt += 1 # Counting frames

    if ret==True:
        crop_frame = frame[y:y+h, x:x+w]

        out.write(crop_frame)
          
        cv2.imshow('frame',frame)
        cv2.imshow('cropped',crop_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()