import cv2
import os

# read video
video_path = os.path.join(".", "sample.mp4")

video = cv2.VideoCapture(video_path)

# visualize video
return_value = True
while return_value: 
    return_value, frame = video.read() #.read() is a tuple, returns bool for return_value and data for frame

    if return_value: #ensure theres a valid frame
        cv2.imshow('frame', frame)
        cv2.waitKey(40) #wait time is the frame rate (eg. 1000s/25fps = 40ms per frame)

video.release() #release the memory allocated for video
cv2.destroyAllWindows() #always add these 2 lines after calling a video