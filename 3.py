import cv2
import matplotlib.pyplot as plt

imgWin ="C:\\images\\a1.jpg"
img1=cv2.imread(imgWin,1)
img2=abs(255-img1)

histr=cv2.calcHist([img],[0],none,[256],[0,256])
plt.plot(histr)
plt.show()

titles=['Orignals Images','Negative Image']
images=[img1,img2]
for k in range(2):
    plt.subplot(1,2,k+1)
    plt.imshow(images[k],cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
plt.show()