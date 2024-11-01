import cv2
def display_counts(frame, left_count, right_count):
    text = f"Left: {left_count} | Right: {right_count}"
    cv2.putText(frame, text, (1000, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (64, 50, 168), 2)

