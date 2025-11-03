import cv2, os
input_folder="original_images"
output_folder="output_images"
image_name=cv2.imread(r"C:\Users\ansh\Desktop\Python\Helloai\opencv\example.jpg")
input_path=os.path.join(input_folder,image_name)
output_path=os.path.join(output_folder,"annotated_"+image_name)
img=cv2.imread(input_path)
if img is None:raise FileNotFoundError(f"Could not load image from {input_path}")
height,width,_=img.shape
arrow_color=(0,255,0)
thickness=2
tip_length=0.05
y_mid=height//2
left_start=(0,y_mid)
left_end=(width//2-10,y_mid)
right_start=(width-1,y_mid)
right_end=(width//2+10,y_mid)
cv2.arrowedLine(img,left_start,left_end,arrow_color,thickness,tipLength=tip_length)
cv2.arrowedLine(img,right_start,right_end,arrow_color,thickness,tipLength=tip_length)
text=f"Width: {width}px"
font=cv2.FONT_HERSHEY_SIMPLEX
font_scale=0.8
text_color=(255,255,255)
text_thickness=2
text_size=cv2.getTextSize(text,font,font_scale,text_thickness)[0]
text_x=(width-text_size[0])//2
text_y=y_mid-10
cv2.putText(img,(text_x,text_y),font,font_scale,text_color,text_thickness,cv2.LINE_AA)
os.makedirs(output_folder,exist_ok=True)
cv2.imwrite(output_path,img)
print(f"Annotated image saved to: {output_path}")
