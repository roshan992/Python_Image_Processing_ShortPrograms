import os
import cv2

vid=cv2.VideoCapture('D:\\new\\video.mp4')
file_name="D:\\new\\video.mp4"
file_stats = os.stat(file_name)
print(file_stats)
print('file size in bytes:',file_stats.st_size)
print('file size in megabytes:',file_stats.st_size/(1024*1024))
