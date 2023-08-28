import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("C:\\images\\2.jpg",0)
k2=np.array(([0,-1,0],[-1,4,-1],[0,-1,0]),np.float32)
print(k2)
output=cv2.filter2D(img,-1,k2)

plt.subplot(1,2,1)
plt.imshow(img,'gray')
plt.title('Original Image')
plt.subplot(1,2,2)
plt.imshow(output,'gray')
plt.title('Filtered Image')
plt.show()