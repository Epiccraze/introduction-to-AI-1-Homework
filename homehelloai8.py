import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. Load the Image
image_path = os.path.join(r"C:\Users\ansh\Desktop\cropimage\AIEPCM2L2 Activities Boilerplate code\example.jpg")
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Image not found. Check your path or filename.")

# 2. Convert the Image to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Display the Grayscale Image
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

# 4. Crop the Image
# Define a region of interest [y1:y2, x1:x2]
cropped_image = image[100:300, 200:400]

# 5. Rotate the Image by 45 degrees
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# 6. Adjust the Brightness
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50  # Increase brightness by 50
bright_image = cv2.add(image, brightness_matrix)

# 7. Save the Output Images
output_dir = 'output_images'
os.makedirs(output_dir, exist_ok=True)

cv2.imwrite(os.path.join(output_dir, 'grayscale.jpg'), gray_image)
cv2.imwrite(os.path.join(output_dir, 'cropped.jpg'), cropped_image)
cv2.imwrite(os.path.join(output_dir, 'rotated.jpg'), rotated_image)
cv2.imwrite(os.path.join(output_dir, 'brightened.jpg'), bright_image)

print("All processed images have been saved in the 'output_images' folder.")

# 8. Documentation
"""
This script loads an image from the 'example.jpg' folder and performs several transformations:
1. Converts it to grayscale.
2. Crops a region of interest.
3. Rotates it by 45 degrees.
4. Increases its brightness.
"""
