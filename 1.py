import cv2
img=cv2.imread("C:\\images\\a1.jpg",0)
outpath="C:\\images\\a11.jpg"
cv2.imshow('lena',img)
cv2.imwrite(outpath,img)
cv2.waiKey(0)
cv2.destoryAllWindows()