import os
import os.path


file = []
for root, dirs, files in os.walk("folder1", topdown=True):
    for f in files:
        path = os.path.join(root, f)
        file.append(path)

for root, dirs, files in os.walk("folder1", topdown=True):
    for d in dirs:
        path = os.path.join(root, d)
        file.append(path)

print(file)