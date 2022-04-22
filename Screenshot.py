# Python program to take
# screenshots


import numpy as np
import cv2
import pyautogui
import os
#test
#shit


# take screenshot using pyautogui


#image = pyautogui.screenshot() IMPORTANT

# since the pyautogui takes as a
# PIL(pillow) and in RGB we need to
# convert it to numpy array and BGR
# so we can write it to the disk


#image = cv2.cvtColor(np.array(image),
					#cv2.COLOR_RGB2BGR) #IMPORTANT

# writing it to the disk using opencv


#cv2.imwrite("image4.png", image) can be done with path instead as first parameter IMPORTANT

for dirpath, dirnames, filenames in os.walk(r".//views.py//Pod1//"):
	for file in filenames:
		filee="C:\\Users\\capta\\dev\\LCSPods\\FinalShowcaseGenerator\\views.py\\Pod1\\"+str(file)
		os.startfile(filee)
		image = pyautogui.screenshot()
		image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
		cv2.imwrite(str(file)+".png", image)



