import cv2
print(cv2.__version__)
import numpy as np

RECT_WIDTH = 107
RECT_HEIGHT = 48
VIDEO_PATH = "carPark.mp4"

CAR_PARK_POSITIONS = []
EMPTY_PARKS = []


def mouse_click(event, x, y, flags, params):
    global CAR_PARK_POSITIONS, EMPTY_PARKS
    if event == cv2.EVENT_LBUTTONDOWN:
        EMPTY_PARKS.append((x, y))
        print(f"Boş park yeri işaretlendi: ({x}, {y})")

        cv2.rectangle(frame, (x, y), (x + RECT_WIDTH, y + RECT_HEIGHT), (0, 255, 0), 2)
        cv2.imshow("Park Alanı Seçimi", frame)


def main():
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Hata: Video dosyası açılamadı.")
        return

    ret, frame = cap.read()
    if not ret:
        print("Video başlatılamadı.")
        return

    cv2.imshow("Park Alanı Seçimi", frame)
    cv2.setMouseCallback("Park Alanı Seçimi", mouse_click)

    print("Lütfen boş park alanlarını işaretleyin (Çıkmak için 'q' tuşuna basın).")

    while True:

        ret, frame = cap.read()
        if not ret:
            print("Video sonu veya okuma hatası.")
            break

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

        for (x, y) in EMPTY_PARKS:
            cv2.rectangle(frame, (x, y), (x + RECT_WIDTH, y + RECT_HEIGHT), (0, 255, 0), 2)

        cv2.imshow("Park Alanı Seçimi", frame)

    cap.release()
    cv2.destroyAllWindows()

    print(f"İşaretlenen boş park yerleri: {EMPTY_PARKS}")


if __name__ == "__main__":
    main()