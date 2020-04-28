import cv2
import numpy as np

p = cv2.VideoCapture(0)
if(p.isOpened()==False):
   print("Unable to read camera")
while True:
        status , photo = p.read()  #click the photo"
        photo = cv2.resize(photo,(300,300))
        (h,w) = photo.shape[0:2]
        zeros = np.zeros((h,w),dtype="uint8")
        B, G, R = cv2.split(photo)
        R = cv2.merge((zeros, zeros, R))
        G = cv2.merge((zeros, G, zeros))
        B = cv2.merge((B, zeros, zeros))
        output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
        output[0:h, 0:w] = photo
        output[0:h, w:w * 2] = R
        output[h:h * 2, w:w * 2] = G
        output[h:h * 2, 0:w] = B
        output = cv2.resize(output,(300,300))
        cv2.imshow('main',photo)
        cv2.imshow('filter',output)
        if cv2.waitKey(10) == 13:         #wait for 10 ms and then keep going but it will give flactuate output(do destroy out of loop)
           break                          # 13 == ENTER KEY (press this and terminate the live capturing)
p.release()
cv2.destroyAllWindows()

