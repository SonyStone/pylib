import os

def fileFind(folder, name):
    result = []
    for root, dirs, files in os.walk(folder):
        if name in files:
            result.append(os.folder.join(root, name))
    return result