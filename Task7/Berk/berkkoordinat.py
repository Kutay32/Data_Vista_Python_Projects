import cv2
import numpy as np

PARKING_SPOT_SIZE = (107, 48)
VIDEO_SOURCE = "carPark.mp4"

marked_positions = []
selected_parking_spots = []


def handle_mouse_click(event, x, y, flags, param):
    global marked_positions, frame

    if event == cv2.EVENT_LBUTTONDOWN:
        selected_parking_spots.append((x, y))
        print(f"Park yeri işaretlendi: ({x}, {y})")

        cv2.rectangle(frame, (x, y),
                      (x + PARKING_SPOT_SIZE[0], y + PARKING_SPOT_SIZE[1]),
                      (0, 255, 0), 2)  # Yeşil çerçeve
        cv2.imshow("Park Alanı Seçimi", frame)

        if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(pos_list):
            x1, y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                pos_list.pop(i)
                
def initialize_parking_spot_selection(video_path):
    global frame
    video = cv2.VideoCapture(video_path)
    if not video.isOpened():
        print("Hata: Video dosyasına erişilemiyor.")
        return
    success, frame = video.read()
    if not success:
        print("Hata: Video başlatılamadı.")
        video.release()
        return
    cv2.imshow("Park Alanı Seçimi", frame)
    cv2.setMouseCallback("Park Alanı Seçimi", handle_mouse_click)
    print("Boş park alanlarını seçmek için fareyle işaretleyin. Çıkış için 'q' tuşuna basın.")
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        for (x, y) in selected_parking_spots:
            cv2.rectangle(frame, (x, y),
                          (x + PARKING_SPOT_SIZE[0], y + PARKING_SPOT_SIZE[1]),
                          (0, 255, 0), 2)
        cv2.imshow("Park Alanı Seçimi", frame)
    video.release()
    cv2.destroyAllWindows()
    print(f"İşaretlenen park yerleri: {selected_parking_spots}")

if __name__ == "__main__":
    initialize_parking_spot_selection(VIDEO_SOURCE)