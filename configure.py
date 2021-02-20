from os.path import isfile, isdir
import os

if not isfile("ezpz"):
	print("Main Script Not Found!")
	exit(1)

if not isfile("fetchData"):
	print("fetchData File Not Found")
	exit(1)

if not isdir(f"{os.environ['PREFIX']}/.config"):
	os.system(f"mkdir {os.environ['PREFIX']}/.config")
	os.system(f"mkdir {os.environ['PREFIX']}/.config/ezpz")

os.system(f'termux-fix-shebang ezpz')
os.system(f'termux-fix-shebang fetchData')
os.system(f"cp fetchData {os.environ['PREFIX']}/.config/ezpz/")

if isfile(f"{os.environ['PREFIX']}/.config/ezpz/fetchData"):
	print("SuccessFully Configured!")