#!/data/data/com.termux/files/usr/bin/env python3

import sys, os
# ________________________________

__author__ = 'Visto-Preto'
__version__ = '1.0.0'
def platform():
	if sys.platform == 'linux':
		os_cls = 'clear' 
		red = '\033[1;31m' 
		green = '\033[1;32m' 
		yellow = '\033[1;33m' 
		blue = '\033[1;34m' 
		magenta = '\033[1;35m' 
		cyan = '\033[1;36m' 
		reset = '\033[m'
		delete = 'rm -rf'


	elif sys.platform == 'win32':
		os_cls = 'cls' 
		red = '' 
		green = '' 
		yellow = '' 
		blue = '' 
		magenta = '' 
		cyan = '' 
		reset = ''
		delete = 'del /f'
	return os_cls, red, green, yellow, blue, magenta, cyan, reset, delete
