#file detection

import os
path="C:\\sample\\test.txt"
if os.path.exists(path):
    print("The location exists")
    if os.path.isfile(path):
        print("This is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That loc does not exists")