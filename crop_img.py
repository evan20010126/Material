import cv2
# 230x420
name = "knife.jpg"
try:
    img = cv2.imread(name)
except:
    print("no")
    exit()

# 裁切區域的 x 與 y 座標（左上角）
x = 305
y = 339

# 裁切區域的長度與寬度
# w = 535
w = 613
# h = 467
h = 535

# 裁切圖片
crop_img = list()
crop_img = img[y:y+h, x:x+w]

cv2.imwrite("modify" + name, crop_img)

# 進去去背後535x467
