from pathlib import Path
import cv2
from cv2 import imshow
import numpy as np
import glob


def createVideo(imagesPath: Path):
    frameSize = (500, 500)
    out = cv2.VideoWriter('asdfasdf.avi',cv2.VideoWriter_fourcc(*'DIVX'), 60, frameSize)

    for path in Path(imagesPath).iterdir():
        if path.is_file() and path.suffix == '.jpg':
            print(path)
            img = cv2.imread(str(path))
            imshow(str(path), img)
            out.write(img)
            
    out.release()


def main():
    cwd = Path().absolute()
    dataPath = Path(cwd / 'assignments/assignment01/data')
    imagesPath = dataPath / 'images'
    createVideo(imagesPath=imagesPath)

if __name__ == '__main__':
    main()