import cv2
import numpy as np
from matplotlib import pyplot as plt
import Tkinter, tkFileDialog

root = Tkinter.Tk()
root.withdraw()

# Dialogue box to choose image files for comparison
print("""A dialogue box will open.
First, choose your main image.
Second, choose the image to find in the main image.""")

mainImage = tkFileDialog.askopenfilename()
capture = tkFileDialog.askopenfilename()

colour = raw_input("Choose a color (type 'red', 'green' or 'blue'): ")

# Determine colour of highlight boxes
if colour == "red":
	colour = (0,0,255)
elif colour == 'green':
	colour = (0,255,0)
elif colour == 'blue':
	colour = (255,0,0)

# Image comparison
mainImage = cv2.imread(mainImage)
mainImageGray = cv2.cvtColor(mainImage, cv2.COLOR_BGR2GRAY)
capture = cv2.imread(capture,0)
w, h = capture.shape[::-1]

res = cv2.matchTemplate(mainImageGray,capture,cv2.TM_CCOEFF_NORMED)
num = raw_input("Choose a similarty percentage for comparison i.e. 0.5 is 50%: ")
threshold = float(num) 
#threshold = 0.8
loc = np.where( res >= threshold )
for pt in zip(*loc[::-1]):
    cv2.rectangle(mainImage, pt, (pt[0] + w, pt[1] + h), (colour), 2)
	
print("A file named 'result.png' will now be in your directory.")

cv2.imwrite('result.png',mainImage)
