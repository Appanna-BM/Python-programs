import os 
src="test.txt"
dst="C:\\sample\\test.txt"

try:
    if os.path.exists(dst):
        print("There is already a file there")
    else:
        os.replace(src, dst)
        print(src+" was moved")
except FileNotFoundError:
    print(src + " was not found")