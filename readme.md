# Mini project: Nhận diện xe cộ và đếm số lượng

Dự án này phát hiện, đếm và theo dõi các phương tiện trong video, đặc biệt tập trung vào các phương tiện trong các làn đường riêng biệt và đếm chúng khi chúng đi qua một khu vực cụ thể.Thư viện OpenCV được sử dụng để xử lý hình ảnh và phát hiện đường viền, cùng với logic tùy chỉnh để theo dõi các đối tượng và tránh đếm trùng lặp. Dự án này không sử dụng mô hình deep learning để nhận điện và theo dõi đối tượng nên độ chính xác trong dự án này có thể chưa cao và cần phải cải tiến thêm sau này. Video đã xử lý được lưu dưới dạng tệp đầu ra ở định dạng `.mp4`.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features](#features)
- [Configuration](#configuration)
- [Example Output](#example-output)

## Installation
### Requirements

1. Tải môi trường  [Python 3.10+](https://www.python.org/downloads/)
2. Tải các thư viện cần cho dự án :
    - `opencv-python`
   - `numpy`
### Clone the Repository
Clone the repository to your local machine:
```bash
   git clone https://github.com/Tranngocphuc2003/Mini_project2-Simple_object_detection.git
    cd Mini_project2-Simple_object_detection
```
## Usage
1. Chuẩn bị video: Đặt video đầu vào vào thư mục `video/`và cập nhật đường dẫn vào trong code nếu cần.
2. Chạy chương trình: Chạy file `main.py` để bắt đầu quá trình phát hiện xe và lưu video đầu ra:
```bash
python main.py
```
3. Video đầu ra: video đã được xử lý sẽ được lưu trong đường dẫn `output/output_video.mp4`.

## Project Structure
```
Mini_project2-Simple_object_detection/
├── video/
│   └── input_video.mp4     # Input video file
├── output/
│   └── output_video.mp4    # Output video file
├── main.py                 # File chính cho việc phát hiện và đếm xe
├── config.py                        
├── src/
│   ├── display.py
│   ├── tracking.py
│   ├── vehicle_detector.py
│   └── video_processing.py
├── README.md               # Tài liệu dự án
├── mini_project2.pdf       # Minh hoạ project
└── requirements.txt        # Thư viện cần dùng
```
### main.py
Đây là file chính để chạy chương trình, có chức năng:
- Xử lý từng khung hình video để phát hiện phương tiện.
- Theo dõi phương tiện bằng cách khớp tâm.
- Vẽ các bouding-box xung quanh phương tiện được phát hiện.
- Đếm số lượng xe nằm trong vùng diện tích giới hạn được định sẵn ở làn đường bên trái và bên phải và hiện thị số lượng theo thời gian thực.
- Lưu video đã được xử lý với bouding-box và bộ đếm.

## Features
- Phát hiện xe cộ: Phát hiện xe cộ dựa vào contours và lọc dựa trên diện tích và hình dạng.
- Bouding-box: Vẽ bouding-box xung quanh các phương tiện được phát hiện, cập nhật theo thời gian thực.
- Đếm xe: Đếm số xe ở làn đường bên trái và bên phải được chỉ định, hiển thị số lượng trong video.
- Theo dõi hướng: Xác định hướng di chuyển và thay đổi màu của bouding-box dựa trên hướng đó.
- Tạo video đầu ra: Lưu video đã xử lý dưới định dạng `.mp4`.

## Configuration
Bạn có thể điều chỉnh các tham số sau trong `config.py`:
- `min_contour_width`, `min_contour_height`: Kích thước tối thiểu của các đối tượng được phát hiện để lọc nhiễu.
- `min_area`, `max_area`: Ngưỡng diện tích hộp giới hạn để giới hạn kích thước xe.
- `line_position`: Đặt vị trí của đường ngang để đếm số lượng xe.
- `frame_countdown`: Thời gian tính theo khung hình để giữ lại tâm của vật thể để theo dõi.
- `max_distance`: Khoảng cách tối đa để xác định xe cùng loại.

## Example Output
Video kết quả sẽ hiển thị: 
- Bouding-box xung quanh xe.
- Số lượng xe ở mỗi làn đường (Left: X| Right:Y)
- Màu sắc của bounding-box thay đổi tương ứng với hướng của xe.

### Video demo
![Vehicle Detection Demo](output/output_video.gif)
