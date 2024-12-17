import cv2
import numpy as np

RECT_WIDTH = 100
RECT_HEIGHT = 40
THRESHOLD = 650

CAR_PARK_POSITIONS = [
(59, 99), (61, 149),(49, 198),(62, 238), (51, 283),
(43, 340), (47, 386), (51, 428), (52, 471), (59, 519),
(48, 570),(48, 628), (166, 104), (166, 144), (166, 190),
(164, 237),(163, 295), (166, 335), (161, 373),(167, 436),
(171, 485), (170, 530), (168, 576), (162, 626),(394, 96),
(393, 144), (403, 198), (406, 244), (406, 287),(404, 333),
(408, 385), (406, 434), (409, 528), (402, 572),(397, 625),
(509, 95),(507, 245), (511, 296), (514, 331),(518, 378),
(515, 431),(510, 147), (511, 198), (753, 85), (757, 131),
(755, 181), (752, 231),(508, 617), (514, 574),(508, 531),
(750, 610), (759, 572), (759, 525), (747, 468),(744, 426),
(745, 384), (747, 333), (752, 279), (901, 146),(901, 194),
(906, 238), (913, 285), (917, 329), (914, 375),(900, 624),
(903, 575), (903, 525), (910, 480), (912, 428),(459, 481)
]

VIDEO_PATH = "carPark.mp4"


def process_frame(frame, positions, rect_width, rect_height):
    processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    processed_frame = cv2.GaussianBlur(processed_frame, (3, 3), 1)


    thresholded = cv2.adaptiveThreshold(processed_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          cv2.THRESH_BINARY_INV, 25, 16)
    i_thresholded = cv2.medianBlur(thresholded, 5)

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
        print("error: Video file could not be opened.")
        return

    print("Parking detection started. Press 'q' to exit or 's' to save the frame.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video or read error.")
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
            print("Image saved: output.jpg")

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()