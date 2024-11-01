import cv2
import numpy as np
from src.display import display_counts
import config
def process_video(video_path, detector, tracker):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Cấu hình ghi video đầu ra
    output_path = "output\\output_video.mp4"
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Mã codec cho định dạng mp4
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    if cap.isOpened():
        ret, frame1 = cap.read()
    else:
        ret = False
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    while ret:
        d = cv2.absdiff(frame1, frame2)
        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(grey, (3, 3), 0)

        ret, th = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(th, np.ones((4, 4)), iterations=2)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
        opening = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        contours, h = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(
            frame1,
            (0, height // 2),
            (width, height // 2),
            (0, 255, 0),
            2,
        )
        cv2.line(
            frame1,
            (0, config.line_position),
            (width, config.line_position),
            (0, 0, 255),
            2,
        )
        detected_centroids =detector.detect_vehicle(frame1, closing)
        left_count, right_count = tracker.update_tracks(detected_centroids, width)

        display_counts(frame=frame1, left_count=left_count, right_count=right_count)
        out.write(frame1)
        cv2.imshow("Vehicle Detection", frame1)
        if cv2.waitKey(40) & 0xFF == ord("q"):
            break
        frame1 = frame2
        ret, frame2 = cap.read()
    cap.release()
    cv2.destroyAllWindows()
