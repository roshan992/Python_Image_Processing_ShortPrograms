import cv2
vid=cv2.VideoCapture('D:\\new\\video.mp4')

print("Width",vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height",vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("FPS",vid.get(cv2.CAP_PROP_FPS))
print("Count",vid.get(cv2.CAP_PROP_FRAME_COUNT))