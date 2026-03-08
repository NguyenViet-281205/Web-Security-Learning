## Hướng dẫn cài đặt và vận hành hệ thống

### Bước 1: Cài đặt môi trường cốt lõi và tải mã nguồn
*   Truy cập trang chủ [Python.org](https://www.python.org/downloads/), tải và cài đặt Python 3 (khuyến nghị từ bản 3.8 đến 3.12). 
    > **Lưu ý quan trọng:** Trong quá trình cài đặt trên Windows, bắt buộc phải đánh dấu vào hộp kiểm **"Add Python to PATH"** để hệ điều hành có thể nhận diện lệnh `python` trên Terminal.
*   Mở Terminal/Command Prompt và kiểm tra lại phiên bản bằng lệnh:
    ```bash
    python --version
    ```
*   Bổ sung: Tải phần mềm soạn thảo mã nguồn VS Code tại: [Visual Studio Code](https://code.visualstudio.com/download)
*   Sử dụng lệnh `git clone` hoặc tải trực tiếp mã nguồn dự án về máy:
    ```bash
    git clone https://github.com/NguyenViet-281205/Web-Security-Learning.git
    ```

### Bước 2: Cài đặt các thư viện phụ thuộc
File `requirements.txt` trong dự án đã cấu trúc sẵn danh sách các gói cần thiết. Việc cập nhật các gói này diễn ra hoàn toàn tự động.
*   Chạy công cụ pip (Package Installer for Python) để kết nối tới PyPI và tải các thư viện vào môi trường ảo hiện tại của dự án:
    ```bash
    pip install -r requirements.txt
    ```

### Bước 3: Khởi tạo Database ban đầu (Database Initialization)
Dự án sử dụng cơ sở dữ liệu SQLite gọn nhẹ. Các bạn không cần thiết lập máy chủ phức tạp (hay cấu hình user/password), kịch bản `init_db.py` sẽ thực thi mọi công việc bao gồm việc tái tạo bảng và chèn sẵn dữ liệu mẫu (hơn 100 sản phẩm đa đạng ngành hàng: điện tử, phần cứng, đồ gia dụng...).
*   Chạy lệnh nạp cơ sở dữ liệu:
    ```bash
    python init_db.py
    ```
*   *Kết quả thành công:* Màn hình sẽ hiển thị thông báo hoàn tất, kèm theo đó là một file `database.db` tự động được sinh ra trong cùng thư mục dự án.

### Bước 4: Kích hoạt máy chủ và thử nghiệm hệ thống
Để khởi động hệ thống web framework (Flask), ta gọi file mã nguồn trung tâm.
*   Chạy lệnh khởi động ứng dụng:
    ```bash
    python app.py
    ```
*   Theo cấu hình mặc định, server sẽ lắng nghe ở port `5000`. Hãy mở trình duyệt, điều hướng tới **một trong hai** liên kết sau:
    *   [http://127.0.0.1:5000](http://127.0.0.1:5000)
    *   [http://localhost:5000](http://localhost:5000)
    
👉 Tiến hành thử nghiệm bằng cách truy cập vào trang **Login** hoặc **Products** để tận mắt xem kiến trúc phản hồi của ứng dụng.
