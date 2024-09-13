#!/usr/bin/python3

import os

libs = {"numpy", "jieba", "pyqt5", "django", "pandas", "docopt", "pygame"}

try:

	for lib in libs:

		os.system("pipx install " + lib)

	print("Successful")

except:

	print("Failed Somehow")


