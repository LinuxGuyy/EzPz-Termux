import os
from os.path import isfile, expanduser

if not isfile(f"{expanduser('~')}/.bashrc"):
	print('.bashrc Not Found, Making One For You')

print("Installing EzPz")
if not isfile('ezpz'):
	print('"EzPz Script Not Found !!!"')
	exit(1)

os.system(f'chmod 777 ezpz')
os.system(f'termux-fix-shebang ezpz')
os.system(f'cp ezpz $PREFIX/bin/')

with open(f"{expanduser('~')}/.bashrc", 'a') as f:
	f.write('\n\nezpz')

print("To Remove From Run On Boot goto github.com/LinuxGuyy/EzPz-Termux")