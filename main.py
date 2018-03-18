import cv2
import input.keyboard as keyboard
import input.mouse as mouse
import output.screen as screen
import vision.hudinfo as hud
from time import sleep
import random

def main():
	#screen_out = screen.grab()
	#screen_gray = cv2.cvtColor(screen_out, cv2.COLOR_BGR2GRAY)
	sleep(1)
	while True:
		if 'Q' in keyboard.get_pressed_keys():
			break
		mouse.left_click(580,302)
		variance = random.randrange(0, 50) / 100
		sleep(0.15 + variance)

if __name__ == '__main__':
	main()
	