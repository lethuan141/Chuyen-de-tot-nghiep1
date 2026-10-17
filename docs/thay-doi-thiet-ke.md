\# NHẬT KÝ THAY ĐỔI THIẾT KẾ – BUỔI 08



\## 1. Thông tin chung

\- Dự án: Smart CRM – Mekong Mobile

\- Luồng nghiệp vụ: L2 – Tiếp nhận và phân loại yêu cầu bảo hành

\- Track: SE

\- Kiến trúc: Layered Architecture

\- Công nghệ dự kiến: Python, FastAPI, MySQL



\## 2. Phản hồi BT1 từ giảng viên

\- Phản hồi của giảng viên: \[Ghi nội dung phản hồi thực tế]

\- Trạng thái tiếp nhận: \[Đã đọc / Đang chờ phản hồi]



\## 3. Quyết định thiết kế

\- Giữ nguyên kiến trúc phân lớp gồm routes, services và repositories vì giúp tách biệt API, nghiệp vụ và truy cập dữ liệu.

\- Giữ mô hình MySQL và các thực thể đã xác định trong BT1.

\- Triển khai migration để tạo bảng theo thiết kế dữ liệu.

\- Bổ sung dữ liệu seed để kiểm thử các chức năng tiếp nhận bảo hành.

\- Hiện thực CRUD cho entity chính, đồng thời kiểm tra khóa ngoại và tính duy nhất của mã phiếu bảo hành.



\## 4. Các điểm cần kiểm chứng

\- Xác nhận DDL khớp với mô hình dữ liệu BT1.

\- Xác định quy tắc tính SLA theo mức ưu tiên và lịch làm việc.

\- Kiểm tra quy tắc ngăn tạo phiếu đang xử lý trùng thiết bị.

\- Kiểm tra khả năng tra cứu khách hàng bằng số điện thoại và thiết bị bằng Serial/IMEI.



\## 5. Lý do kỹ thuật

Việc giữ kiến trúc phân lớp giúp mã nguồn dễ kiểm thử, bảo trì và mở rộng. Migration giúp quản lý cấu trúc cơ sở dữ liệu có phiên bản; seed giúp kiểm thử lặp lại với dữ liệu mẫu.



\## 6. Trạng thái thực hiện

\- Cấu trúc thư mục: \[Cập nhật sau khi kiểm tra]

\- Migration và seed: \[Cập nhật sau khi thực hiện]

\- CRUD: \[Cập nhật sau khi kiểm thử]

\- Ảnh minh chứng: \[Bổ sung đường dẫn ảnh]

\- Commit cuối buổi: \[Bổ sung URL commit]



