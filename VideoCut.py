import cv2
import sys

from numpy import true_divide

# parser = argparse.ArgumentParser()
# parser.add_argument("--video")
# args = parser.parse_known_args()
try:
    sys_input = sys.argv[1]
except:
    print("Error: You didn't input video.")
    exit()

video = cv2.VideoCapture(sys.argv[1])
vd_write = cv2.VideoWriter(sys.argv[0] + "01.avi", cv2.VideoWriter_fourcc(*'XVID'), video.get(cv2.CAP_PROP_FPS),
                           (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))

count = -1

total = video.get(cv2.CAP_PROP_FRAME_COUNT)

while count < (total/2):
    count += 1
    ret, frame = video.read()
    if ret == False:
        break

    print(str(count) + "/" + str(total))
    vd_write.write(frame)

vd_write.release()

vd_write = cv2.VideoWriter(sys.argv[0] + "02.avi", cv2.VideoWriter_fourcc(*'XVID'), video.get(cv2.CAP_PROP_FPS),
                           (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))))

while True:
    count += 1
    ret, frame = video.read()
    if ret == False:
        break

    print(str(count) + "/" + str(total))
    vd_write.write(frame)


video.release()
vd_write.release()
