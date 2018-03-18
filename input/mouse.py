import win32api

# Useful links for mouse event emulation under Windows
# http://timgolden.me.uk/pywin32-docs/win32api__mouse_event_meth.html
# https://msdn.microsoft.com/en-us/library/windows/desktop/ms646260(v=vs.85).aspx

EVENTS = {
	'MOVE_RELATIVE': 0x0001,
	'LEFT_DOWN': 0x0002,
	'LEFT_UP': 0x0004
}

# Moves to absolute coordinates
def move_to(x, y):
	win32api.SetCursorPos((x, y))
	
# Emultates mouse click at given coordinates
def left_click(x, y):
	# Moves mouse at desired coordinates
	move_to(x,y)
	
	# Clicks at current mouse position
	# 2nd and 3rd arguments are ignored but demanded
	win32api.mouse_event(EVENTS['LEFT_DOWN'], 0, 0)
	
	# Release the button
	win32api.mouse_event(EVENTS['LEFT_UP'], 0, 0)
	
def left_dbl_click(x, y):
	left_click(x, y)
	left_click(x, y)
	
if __name__ == '__main__':
	left_click(0,0)