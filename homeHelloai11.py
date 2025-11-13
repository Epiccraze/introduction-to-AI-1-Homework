import cv2
import numpy as np
img=cv2.imread('image.jpg')
tint='r'
r_intensity,g_intensity,b_intensity=1.0,1.0,1.0
def apply_tint(image,tint):
    b,g,r=cv2.split(image)
    if tint=='r':r=cv2.add(r,50)
    elif tint=='g':g=cv2.add(g,50)
    elif tint=='b':b=cv2.add(b,50)
    return cv2.merge((b,g,r))
while True:
    adjusted=img.copy()
    adjusted=cv2.convertScaleAbs(adjusted,alpha=1,beta=0)
    b,g,r=cv2.split(adjusted)
    r=np.clip(r*r_intensity,0,255).astype(np.uint8)
    g=np.clip(g*g_intensity,0,255).astype(np.uint8)
    b=np.clip(b*b_intensity,0,255).astype(np.uint8)
    adjusted=cv2.merge((b,g,r))
    cv2.imshow('Adjust Colors',adjusted)
    k=cv2.waitKey(0)&0xFF
    if k==27:break
    elif k==ord('r'):tint='r';img=apply_tint(img,'r')
    elif k==ord('g'):tint='g';img=apply_tint(img,'g')
    elif k==ord('b'):tint='b';img=apply_tint(img,'b')
    elif k==ord('i'):r_intensity+=0.1
    elif k==ord('d'):b_intensity=max(0,b_intensity-0.1)
    elif k==82:g_intensity+=0.1
    elif k==84:r_intensity=max(0,r_intensity-0.1)
cv2.destroyAllWindows()