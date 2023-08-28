import cv2

vid=cv2.VideoCapture('D:\\new\\video.mp4')

while(vid.isOpened()):
    ret,frame=vid.read()
    if ret== True:
        cv2.imshow('Frame',frame)
        key=cv2.waitKey(20)
        if key == ord('q'):
            break
    else:
         break
vid.release()
cv2.destroyAllWindows()