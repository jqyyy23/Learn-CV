import cv2

#read webcam
webcam = cv2.VideoCapture(0)

#visualize webcam 
while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    #reading frames from webcame requires small delay
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break #stop the webcame when 'q' is preessed

webcam.release()
cv2.destroyAllWindows()