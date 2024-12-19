import cv2
import numpy as np

RECT_DIMENSIONS = (109, 49)
THRESHOLD_LIMIT = 670
VIDEO_FILE = "carPark.mp4"

PARKING_SPOTS = [
(36, 87), (34, 140), (38, 194), (39, 245), (39, 293), (41, 343), (43, 393), (44, 440),
    (40, 489), (39, 532), (32, 580), (34, 628), (156, 97), (156, 145), (155, 197), (160, 241),
    (160, 288), (163, 337), (162, 383), (160, 438), (161, 484), (160, 531), (166, 579), (164, 621),
    (398, 79), (398, 139), (404, 191), (402, 245), (402, 291), (402, 342), (404, 387), (408, 432),
    (408, 525), (408, 576), (413, 620), (514, 78), (519, 137), (518, 193), (517, 236), (519, 289),
    (513, 335), (522, 383), (524, 429), (524, 520), (526, 571), (525, 620), (743, 77), (749, 134),
    (750, 188), (752, 241), (750, 283), (750, 332), (753, 377), (756, 428), (752, 479), (755, 527),
    (755, 573), (752, 617), (896, 141), (900, 189), (904, 237), (907, 284), (908, 334),
    (914, 385), (908, 438), (911, 482), (910, 521), (913, 570), (915, 619)
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