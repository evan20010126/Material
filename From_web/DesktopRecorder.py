# https://www.twblogs.net/a/5c015ec3bd9eee7aed33ab5b
from PIL import ImageGrab
import numpy as np
import cv2

image = ImageGrab.grab()  # 獲得當前屏幕
width = image.size[0]
height = image.size[1]
print("width:", width, "height:", height)
print("image mode:", image.mode)
k = np.zeros((width, height), np.uint8)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 編碼格式
video = cv2.VideoWriter('test.avi', fourcc, 25, (width, height))
# 輸出文件命名爲test.mp4,幀率爲16，可以自己設置
while True:
    img_rgb = ImageGrab.grab()
    img_bgr = cv2.cvtColor(
        np.array(img_rgb), cv2.COLOR_RGB2BGR)  # 轉爲opencv的BGR格式
    video.write(img_bgr)
    cv2.imshow('imm', img_bgr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
