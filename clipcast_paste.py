#!/usr/bin/env python


from pykeyboard import PyKeyboard
k = PyKeyboard()

import pyperclip



text_file = open("<Path to text/Input_paste.txt", "r")
data = text_file.read()
pyperclip.copy(data)

k.press_key(k.control_key)
k.tap_key('v')
k.release_key(k.control_key)

print(data)
text_file.close()



