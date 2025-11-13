import cv2
img = cv2.imread(r"C:\Users\ansh\Desktop\Python\Helloai\opencv\example.jpg")
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cropped = img[0:200, 0:200]
bright = cv2.convertScaleAbs(img, alpha=1, beta=50)
cv2.imshow('Original', img)
cv2.imshow('Rotated', rotated)
cv2.imshow('Cropped', cropped)
cv2.imshow('Bright', bright)
cv2.waitKey(0)
cv2.destroyAllWindows()