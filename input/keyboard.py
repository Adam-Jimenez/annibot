# Keyboard input emulation

# Useful links:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes
import win32api as wapi
import time

SendInput = ctypes.windll.user32.SendInput

KEYS = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
    KEYS.append(char)
	
KEY_CODES = {
	'ESC': 0x01,
	'ENTER': 0x1C,
	'1': 0x02,
	'2': 0x03,
	'3': 0x04,
	'4': 0x05,
	'5': 0x06,
	'6': 0x07,
	'7': 0x08,
	'8': 0x09,
	'9': 0x0A,
	'0': 0x0B,
	'-': 0x0C,
	'=': 0x0D,
	'q': 0x010,
	'w': 0x11,
	'e': 0x12,
	'r': 0x13,
	't': 0x14,
	'y': 0x15,
	'u': 0x16,
	'i': 0x17,
	'o': 0x18,
	'p': 0x19,
	'a': 0x1E,
	's': 0x1F,
	'd': 0x20,
	'f': 0x21,
	'g': 0x22,
	'h': 0x23,
	'j': 0x24,
	'k': 0x25,
	'l': 0x26,
	'z': 0x2C,
	'x': 0x2D,
	'c': 0x2E,
	'v': 0x2F,
	'b': 0x30,
	'n': 0x31,
	'm': 0x32,
	',': 0x33,
	'.': 0x34,
	'/': 0x35,
	' ': 0x39
}

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

# emulates a key press
def press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# emulates a key release
def release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# immediately presses and releases a key
def tap_key(hexKeyCode):
	press_key(hexKeyCode)
	release_key(hexKeyCode)
	
# emulates a word being typed out
def type(word):
	for char in word:
		tap_key(KEY_CODES[char])
		
# returns a list of pressed keys on the keyboard
def get_pressed_keys():
	keys = []
	for key in KEYS:
		if wapi.GetAsyncKeyState(ord(key)):
			keys.append(key)
	return keys
