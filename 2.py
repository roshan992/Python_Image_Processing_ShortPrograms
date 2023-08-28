import cv2
imgpath="C:\\images\\a1.jpg"
img1=cv2.imread(imgpath,1)

print(type(img1))
print('Image Data Type:=',img1.dtype)
print('row column:=',img1.shape)
print('dimension:=',img1.ndim)
print('Image Size:=',img1.dtype)

(nr,nc,ch)=img1.shape
print('row:=',nr)
print('column:=',nc)
print('channel:=',ch)

cv2.imshow('lena',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()