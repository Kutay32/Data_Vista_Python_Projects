import cv2
import numpy as np

RECT_WIDTH = 107
RECT_HEIGHT = 48
THRESHOLD = 650  # Piksel yoğunluğu eşiği

CAR_PARK_POSITIONS = [
    (45, 94), (46, 141), (45, 188), (47, 237), (48, 284), (51, 332), (52, 385), (53, 430), (53, 480), (55, 526)
    , (50, 573), (52, 622), (160, 620), (160, 576), (162, 524), (160, 477), (161, 428), (163, 384), (163, 330),
    (161, 287), (156, 239), (156, 188), (154, 141)
    , (148, 94), (391, 98), (392, 145), (395, 190), (397, 237), (399, 283), (400, 329), (408, 382), (406, 430),
    (404, 475), (404, 516)
    , (395, 570), (398, 618), (509, 614), (508, 570), (508, 520), (509, 428), (510, 378), (512, 331), (510, 278),
    (508, 235), (505, 181)
    , (498, 92), (497, 135), (744, 82), (743, 127), (748, 179), (751, 228), (753, 276), (753, 329), (754, 375),
    (752, 426), (752, 475), (751, 517)
    , (739, 564), (739, 612), (899, 613), (899, 572), (907, 521), (905, 470), (908, 416), (905, 377), (908, 331),
    (911, 284), (907, 234), (901, 187)

]

VIDEO_PATH = "carPark.mp4"


def process_frame(frame, positions, rect_width, rect_height):
    processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    processed_frame = cv2.GaussianBlur(processed_frame, (3, 3), 1)


    thresholded = cv2.adaptiveThreshold(processed_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY_INV, 25, 16)
    i_thresholded = cv2.medianBlur(thresholded, 5)

    #cv2.imshow("Thresholded Image", thresholded)
    empty_spaces = 0

    for x, y in positions:

        roi = i_thresholded[y:y + rect_height, x:x + rect_width]
        non_zero_count = cv2.countNonZero(roi)

        if non_zero_count < THRESHOLD :
            color = (0, 255, 0)  # Yeşil (Boş)
            empty_spaces += 1
        else:
            color = (0, 0, 255)  # Kırmızı (Dolu)


        cv2.rectangle(frame, (x, y), (x + rect_width, y + rect_height), color, 2)
        print(f"Park Alanı ({x}, {y}): Yoğunluk = {non_zero_count}, Durum = {'Boş' if color == (0, 255, 0) else 'Dolu'}")

    cv2.rectangle(frame, (40, 20), (480, 60), (0, 0, 0), -1)
    return frame, empty_spaces


def main():
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Hata: Video dosyası açılamadı.")
        return

    print("Park durumu tespit başlatıldı. Çıkmak için 'q', kareyi kaydetmek için 's' tuşuna basın.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video sonu veya okuma hatası.")
            break

        annotated_frame, empty_spaces = process_frame(frame, CAR_PARK_POSITIONS, RECT_WIDTH, RECT_HEIGHT)

        cv2.putText(annotated_frame, f"Empty Spaces: {empty_spaces}/{len(CAR_PARK_POSITIONS)}",
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Park Alani Tespiti", annotated_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("output.jpg", annotated_frame)
            print("Görsel kaydedildi: output.jpg")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()