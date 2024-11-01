from src.vehicle_detector import VehicleDetector
from src.tracking import VehicleTracker
from src.display import display_counts
from src.video_processing import process_video
import config

def main():
    detector = VehicleDetector(
        min_contour_height=config.min_contour_height,
        min_contour_width=config.min_contour_width,
        min_area=config.min_area,
        max_area=config.max_area,
        line_position=config.line_position
    )
    tracker = VehicleTracker(
        frame_countdown=config.frame_countdown,
        max_distance=config.max_distance,
    )
    process_video(config.VIDEO_PATH, detector=detector, tracker=tracker)
if __name__ == "__main__":
    main()
