import cv2
import pickle
import numpy as np

cap = cv2.VideoCapture("carPark.mp4")
width, height = 107, 48

with open("car_park_pos", "rb") as f:
    pos_list = pickle.load(f)

def check_parking_space(img_pro):

    space_counter = 0
    total_count = 0
    for pos in pos_list:
        x, y = pos

        total_count+=1

        img_crop = img_pro[y:y+height, x:x+width]
        # cv2.imshow(str(x*y), img_crop)
        count = cv2.countNonZero(img_crop)
        cv2.putText(img, str(count), (x, y + height - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

        if count <900:
            color = (0, 255, 0)
            thickness = 4
            space_counter +=1
        else:
            color = (0, 0, 255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color,thickness)

    cv2.rectangle(img, (40, 20), (480, 60), (0, 0, 0), -1)
    cv2.putText(img, f"Total Empty Space: {space_counter}/{total_count}", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (3, 3), 1)
    img_threshold = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY_INV, 25, 16)
    img_median = cv2.medianBlur(img_threshold,5)

    kernel = np.ones((3, 3), np.uint8)
    img_dilate = cv2.dilate(img_median, kernel, iterations=1)

    check_parking_space(img_dilate)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
