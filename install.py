import os
from os.path import isfile

if not isfile('ezpz'):
	print('"ezpz" Script Not Found !!!')
	exit(1)

os.system(f'cp ezpz $PREFIX/bin/')
os.system(f'chmod 777 $PREFIX/bin/ezpz')