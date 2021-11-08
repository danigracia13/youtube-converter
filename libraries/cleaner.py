import pathlib
import os
import time


def fileCounter():
    file_count = 0
    for path in pathlib.Path("./download/").iterdir():
        if path.is_file():
            file_count += 1

    if file_count >= 5:
        time.sleep(5)
        return cleanPath()
    else:
        exit   

def cleanPath():
    dir = './download/'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


