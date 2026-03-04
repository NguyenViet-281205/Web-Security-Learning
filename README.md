# Web-Security-Learning

Hướng dẫn chi tiết cài đặt và khởi chạy môi trường dự án
Cung cấp phương pháp đa dạng phục vụ từng bối cảnh làm việc, phần này chia ra làm hai quy trình thiết lập: Khởi chạy trực tiếp (Local Machine) và Khởi chạy qua hệ sinh thái ảo hóa Container (Docker).
Cách 1: Triển khai trực tiếp trên máy tính cá nhân
Cách thức này phù hợp khi người dùng muốn trực tiếp thao tác, chỉnh sửa mã nguồn và giám sát realtime qua từng dòng lỗi. Phương pháp mang tính truyền thống cao và dễ debug.
•	B1: Cài đặt môi trường cốt lõi và tải mã nguồn
Truy cập trang chủ Python.org, cài đặt Python 3 (từ bản 3.8 đến 3.12). Trong bước cài đặt Windows, bắt buộc phải chọn hộp kiểm "Add Python to PATH" để hệ điều hành nhận diện lệnh python trên Terminal. Kiểm tra lại bằng lệnh `python --version`.
Truy cập trang chủ Visual Studio Code để cài đặt trình soạn thảo mã nguồn.
Truy cập https://github.com/NguyenViet-281205/Web-Security-Learning.git -> bấm vào Code -> Download Zip-> Giải nén Folder.
•	B2: Cài đặt các thư viện phụ thuộc 
Thay vì tìm cài đặt từng bộ phận, file `requirements.txt` đã cấu trúc sẵn danh sách các packet. Gõ lệnh pip (Package Installer for Python) để tự động liên kết tới mạng PyPI (Python Package Index) để cài đặt thư viện vào môi trường ảo hiện tại:
pip install -r requirements.txt
•	B3: Khởi tạo Database ban đầu (Database Initialization)
Khác với CSDL Server cần tạo user/password phức tạp, với SQLite, kịch bản Python `init_db.py` sẽ thực thi mọi công việc bao gồm: Tái tạo các bảng và vòng lặp chèn khối lượng lớn hơn 100 sản phẩm với đa dạng ngành hàng, giá, thời gian bảo hành từ thiết bị điện tử, phần cứng tới đồ dùng hàng ngày. Chạy lệnh:
python init_db.py
Kết quả trả về thành công nếu màn hình thông báo và một file `database.db` xuất hiện ngay cùng thư mục.
•	B4: Kích hoạt máy chủ và thử nghiệm hệ thống
Để gọi hệ thống Flask, chỉ việc thực thi mã nguồn trung tâm:
python app.py
Theo cấu hình mặc định, Server sẽ dùng port `5000`. Mở ngay trình duyệt web và điều hướng tới đường dẫn `http://127.0.0.1:5000` hoặc `http://localhost:5000` để truy cập trang chủ giao diện người dùng. Tiến hành thử vào trang Login hoặc Products để thấy toàn bộ kiến trúc phản hồi ứng dụng.
Cách 2: Triển khai thông qua môi trường ảo hóa Container (Docker)
Nếu dự án được tích hợp cơ chế Docker, người dùng không cần quan tâm đến máy cấu hình hay phiên bản Python gốc bị sai lệch. Docker đảm bảo bao bọc mọi thư viện, code, và runtime thành chuẩn Image đa nền tảng. Để áp dụng, yêu cầu hệ điều hành đã được cài đặt và kích hoạt sẵn ứng dụng Docker Desktop (Windows/Mac) hoặc Docker Engine (Linux).
•	B1: Tải Image hệ thống (Pulling Docker Image)
Image đóng vai trò như bản chụp hoàn chỉnh (Snapshot) của toàn bộ hệ thống (Hệ điều hành nền Linux tối giản Alpine, Python, mã nguồn Flask, dữ liệu file Database...). Bạn có thể kéo bộ cài tĩnh của web này trực tiếp từ kho lưu trữ về môi trường máy bằng dòng lệnh 
docker pull ngveit05/vulweb
•	B2: Biến hóa Image thành Container hoạt động (Run Container)
Container là môi trường sống thực tế khi Image được khởi chạy. Vì bộ server nội tại trong Container mặc định khép kín và không cho người bên ngoài (máy Host) tùy tiện truy cập, dòng lệnh khởi động cần thiết lập ánh xạ cầu nối mạng ảo (Port Mapping). Lệnh thực thi sẽ là:
docker run -p 5000:5000 --name myvulweb ngveit05/vulweb
Giải thích ý nghĩa thông số:
- Cờ ‘-p 5000:5000’ (Publish): Gắn kết cổng 5000 đại diện cho Trình duyệt ở máy tính bên ngoài với cổng 5000 đại diện cho Flask Server phía trong không gian ảo.
- Cờ ‘--name myvulweb: Đặt tên cho quá trình tiện quản lý (ví dụ như xem tiến trình tên gì) sau này.
- Cờ ‘ngveit05/vulweb’: Là vulnerable web được code ra và đã được đẩy lên Docker Hub
•	B3: Truy cập, Khai thác và Giám sát
Tương tự như cài đặt trên local, mở Browser và truy cập theo hệ địa chỉ URL:
http://localhost:5000
•	B4: Giải phóng tài nguyên và đóng môi trường 
Khi kết thúc giờ nghiên cứu, hệ mô phỏng Container có thể tắt nhanh gọn mà không lưu lại dấu vết rác phần mềm lên hệ điều hành của bạn.
Tạm dừng hoạt động cấp phát: `docker stop myvulweb`
Tháo dỡ Container: `docker rm -f myvulweb`

