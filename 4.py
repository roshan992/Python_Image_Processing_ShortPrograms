import cv2
import matplotlib.pyplot as plt

imgWin ="C:\\images\\a1.jpg"
c=1
im=img1/255.0
im1=c*cv2.pow(im,0.6)
im2=c*cv2.pow(im,0.4)
im3=c*cv2.pow(im,0.3)

titles=['Orignals Images','gamma=0.6','gamma=0.4','gamma=0.3']
images=[im,im1,im2,im3]
for k in range(4):
    plt.subplot(1,4,k+1)
    plt.imshow(images[k],cmap='gray')
    plt.title(titles[k])
    plt.xticks([])
    plt.yticks([])
plt.show()