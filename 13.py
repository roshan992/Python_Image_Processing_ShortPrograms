import cv2
import numpy as np
import matplotlib.pyplot as plt

imgpath='C:\\images\\2.jpg'
img = cv2.imread(imgpath, 0)

imgsize=img.shape
print(imgsize)
(nr,nc)=img.shape

cv2.imshow('Orignal Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows('Orignal Image')

a=[]
samplerate=20

x=int(img.shape[0]/samplerate)
y=int(img.shape[1]/samplerate)
for i in range(0,range(0,img.shape[0],samplerate)):
    for j in range(0,range(0,img.shape[1],samplerate)):
        a.append(img[i][j])
        b=np.reshape(a,(x,y))
        bsize=b.shape
        print(bsize)
        cv2.imshow('Output Image',b)
        cv2.waitKey(0)
        cv2.destroyAllWindow('Output Image')
        imgRsz=cv2.resize(b(nr,nc),cv2.INTER_CUBIC)
        cv2.imshow('output Resized Image',imgRsz)
        cv2.waitKey(0)
        cv2.destroyAllWindow('Output resized Image')
