import os
import os.path


for root, dirs, files in os.walk("Work", topdown=True):
    for f in os.listdir(root):
        path = os.path.join(root, f)
        if os.path.isfile(path) and os.path.getsize(path) != 0:
            print(f'{path} - {os.path.getsize(path)} bytes')











