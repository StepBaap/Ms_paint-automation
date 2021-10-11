import pyautogui as gui
import numpy as np
import time
import cv2 as cv

def auto_thresh_canny(image, sigma=0.33):
	# compute the median of image pixels 
	med = np.median(image)
	# apply automatic Canny edge detection using the computed median
	low = int(max(0, (1.0 - sigma) * med))
	high = int(min(255, (1.0 + sigma) * med))
	edge = cv.Canny(image, low, high)
	# return the edged image
	return edge

def Resize(image,h):
	
	(height,width,c) =  image.shape
	aspect_ratio = height/width
	new_width = int(h/aspect_ratio)
	resized_img = cv.resize(image,(new_width,h))
	return resized_img


# Read the original image
img = cv.imread(r"img.jpeg")
#Resize image according to lenght of the canvas in ur pc 
img = Resize(img,600) # height -> 600 pixels
# Convert to graycsale
imgframe_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Blur the image for better edge detection
imgframe_blur = cv.GaussianBlur(imgframe_gray, (3,3), 0) 
# Apply Canny Edge Algo 
img_frame_edged = auto_thresh_canny(imgframe_blur)
# Find contours
frame_contours,hierarchies = cv.findContours(img_frame_edged,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

#automate Ms paint
gui.keyDown('win')
gui.press('r')
gui.keyUp('win')
time.sleep(2)
gui.write('MsPaint')
gui.press('enter')
time.sleep(2)
         
# relative coordinates for the top left image corner to be drawn in the Ms-Paint Canvas         
x0,y0 = 93,105          

for i in range(len(frame_contours)):
	gui.moveTo(frame_contours[i][0][0][0]+x0,frame_contours[i][0][0][1]+y0)
	for j in range(len(1,frame_contours[i])):
		x = frame_contours[i][j][0][0]
		y = frame_contours[i][j][0][1]
		gui.dragTo(x+x0,y+y0,button="left")
		
		
		
