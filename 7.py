import cv2
from matplotlib import pyplot as plt
img=cv2.imread("C:\\images\\a1.jpg")


histr1=cv2.calcHist([img],[0],None,[256],[0,256])
img2=cv2.equalizeHist(img)
histr2=cv2.calcHist([img],[0],None,[256],[0,256])

plt.subplot(221),
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

plt.subplot(222),
plt.plot(histr1),plt.plot(histr2),plt.plot(histr3)
plt.show()

plt.plot(histr)
plt.show()