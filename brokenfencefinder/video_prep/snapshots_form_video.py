"""Module to quickly create some snapshots from a video."""
import cv2
import os


# Read the video from specified path
cam = cv2.VideoCapture("C:\\Users\\Niels\\Documents\\HU\\Jaar2\\BlokC\\bb8\\Data\\test.mp4")

try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

stepSize = 2000

while True:
    if not (currentframe % stepSize == 0):
        currentframe += 1
        continue
    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        print("no ret")
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()


"""
Bron:
https://www.geeksforgeeks.org/extract-images-from-video-in-python/
"""
