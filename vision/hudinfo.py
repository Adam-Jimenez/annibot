import cv2
from PIL import Image
import output.screen as screen
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

# region of screen where location text is found (x, y, x2, y2)
LOCATION_TEXT_REGION = (1300, 35, 1670, 60)

# pytesseract can't be run in git bash for some reason
def get_current_location():
	text_bgr = screen.grab(LOCATION_TEXT_REGION)
	# use hue sat val for color filtering
	text_hsv = cv2.cvtColor(text_bgr, cv2.COLOR_BGR2HSV)
	
	# we specify the range of colors used for the text
	# to remove background
	bgr_lower_color = np.array([50, 50, 50])
	bgr_upper_color = np.array([150, 150, 150])
	
	mask = cv2.inRange(text_hsv, bgr_lower_color, bgr_upper_color)
	filtered_text = cv2.bitwise_and(text_bgr, text_bgr, mask=mask)
	
	# convert to grayscale
	gray_text = cv2.cvtColor(filtered_text, cv2.COLOR_BGR2GRAY)
	
	# make text clearer by applying threshold
	_, threshold_text = cv2.threshold(gray_text, 50, 255, cv2.THRESH_BINARY)
	image = Image.fromarray(threshold_text)
	cv2.imshow('text', threshold_text)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	
	
	text_string = pytesseract.image_to_string(image)
	return text_string