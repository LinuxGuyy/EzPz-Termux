import os
from os.path import isfile

if not isfile(f"{os.environ['PREFIX']}/bin/ezpz"):
	print('"EzPz" is Already Uninstalled')
	exit(1)

os.system(f'rm $PREFIX/bin/ezpz')