import cv2
import numpy as np

RECT_DIMENSIONS = (109, 49)
THRESHOLD_LIMIT = 670
VIDEO_FILE = "carPark.mp4"

PARKING_SPOTS = [(390, 193), (49, 387), (165, 432), (167, 571), (510, 521) ,(902, 145), (750, 331), (754, 377),
                 (756, 475), (757, 563), (909, 524),(901, 476),(41, 101), (39, 146), (41, 194), (42, 244), (42, 289),
                 (44, 339), (46, 434), (44, 480),(50, 530), (47, 570), (43, 617), (162, 622), (166, 532), (166, 476), (159, 385),(741, 85), (739, 135), (739, 183), (742, 231), (748, 280),
                 (739, 426), (747, 523), (752, 617), (913, 621), (912, 571), (913, 426), (908, 380), (903, 329),(909, 235), (910, 183),(153, 98), (149, 140), (153, 186), (157, 236), (159, 286), (162, 334), (163, 428),
                 (389, 91), (390, 147), (386, 186), (392, 240), (399, 291), (396, 337), (396, 385), (399, 433), (404, 518), (399, 565),(389, 91), (390, 147), (386, 186), (392, 240), (399, 291), (396, 337), (396, 385), (399, 433), (404, 518), (399, 565),
                 (502, 95), (504, 142), (503, 193), (505, 234), (512, 282), (512, 327), (514, 374), (507, 420),(896, 285), (509, 571), (512, 618), (407, 617)
]

def analyze_parking_space(frame, spots, dimensions, threshold):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 1)
    binary = cv2.adaptiveThreshold(
        blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )
    binary = cv2.medianBlur(binary, 5)

    empty_count = 0

    for spot in spots:
        x, y = spot
        roi = binary[y:y + dimensions[1], x:x + dimensions[0]]
        pixel_count = cv2.countNonZero(roi)

        if pixel_count < threshold:
            color = (0, 255, 0)
            empty_count += 1
        else:
            color = (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x + dimensions[0], y + dimensions[1]), color, 2)
        print(f"Park Yeri ({x}, {y}): Yoğunluk = {pixel_count}, Durum = {'Boş' if color == (0, 255, 0) else 'Dolu'}")

    return frame, empty_count

def draw_summary(frame, empty_count, total_spots):

    summary_text = f"Empty Spaces: {empty_count}/{total_spots}"
    cv2.rectangle(frame, (10, 10), (500, 60), (0, 0, 0), -1)
    cv2.putText(frame, summary_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    return frame

def process_video(video_path, parking_spots, dimensions, threshold):

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Hata: {video_path} dosyası açılamadı.")
        return

    print("Park yeri analizi başlatıldı. Çıkmak için 'q', kaydetmek için 's' tuşuna basın.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video sonlandı.")
            break

        analyzed_frame, empty_spaces = analyze_parking_space(frame, parking_spots, dimensions, threshold)
        final_frame = draw_summary(analyzed_frame, empty_spaces, len(parking_spots))

        cv2.imshow("Park Yeri Durumu", final_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("output.jpg", final_frame)
            print("Kare kaydedildi: output.jpg")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video(VIDEO_FILE, PARKING_SPOTS, RECT_DIMENSIONS, THRESHOLD_LIMIT)