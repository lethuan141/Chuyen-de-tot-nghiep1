# TEST PLAN – SMART CRM MEKONG MOBILE



## 1. Thông tin chung



- **Dự án:** Smart CRM – Mekong Mobile

- **Luồng nghiệp vụ:** L2 – Tiếp nhận và phân loại yêu cầu bảo hành

- **Loại tài liệu:** Test Plan

- **Phiên bản:** 1.0

- **Ngày cập nhật:** 07/11/2026



## 2. Mục tiêu kiểm thử



- Kiểm tra chức năng tiếp nhận yêu cầu bảo hành.

- Kiểm tra việc tìm kiếm và quản lý thông tin khách hàng.

- Kiểm tra việc quản lý thiết bị theo Serial/IMEI.

- Kiểm tra phân loại yêu cầu bảo hành.

- Kiểm tra xử lý dữ liệu không hợp lệ và các trường hợp ngoại lệ.

- Đảm bảo hệ thống hoạt động đúng theo yêu cầu SRS và API Contract.



## 3. Phạm vi kiểm thử



### 3.1. Trong phạm vi



- API quản lý khách hàng.

- API quản lý thiết bị.

- API quản lý phiếu bảo hành.

- Kiểm tra dữ liệu đầu vào.

- Kiểm tra phản hồi HTTP và thông báo lỗi.

- Kiểm tra tính toàn vẹn dữ liệu.



### 3.2. Ngoài phạm vi



- Kiểm thử hiệu năng quy mô lớn.

- Kiểm thử giao diện trên nhiều thiết bị thực tế.

- Kiểm thử tích hợp với hệ thống bên thứ ba chưa triển khai.



## 4. Môi trường kiểm thử



- **Hệ điều hành:** Windows.

- **Ngôn ngữ:** Python.

- **Backend:** FastAPI.

- **Cơ sở dữ liệu:** MySQL.

- **Công cụ kiểm thử:** Pytest, Postman.

- **Trình duyệt:** Google Chrome.

- **Mã nguồn:** GitHub.



## 5. Chiến lược kiểm thử



Áp dụng kiểm thử chức năng và kiểm thử API.



Các loại kiểm thử bao gồm:



1. **Luồng đúng:** Kiểm tra dữ liệu hợp lệ và nghiệp vụ hoạt động đúng.

2. **Kiểm thử biên:** Kiểm tra dữ liệu ở giới hạn cho phép.

3. **Dữ liệu sai:** Kiểm tra dữ liệu thiếu, sai định dạng hoặc không hợp lệ.

4. **Bảo mật và chất lượng dữ liệu:** Kiểm tra dữ liệu không hợp lệ, trùng lặp và khả năng bảo vệ dữ liệu.

5. **Tái lập:** Chạy lại các trường hợp kiểm thử để xác nhận kết quả ổn định.



## 6. Điều kiện PASS/FAIL



- **PASS:** Kết quả thực tế khớp với kết quả mong đợi.

- **FAIL:** Kết quả thực tế khác với kết quả mong đợi.

- Mỗi Test Case phải có kết quả thực tế và ảnh chụp minh chứng.

- Không tự đánh dấu PASS khi chưa thực hiện kiểm thử.



## 7. Quản lý lỗi



Các lỗi được ghi nhận trong `bug-log.md`, bao gồm:



- Mã lỗi.

- Mô tả lỗi.

- Mức độ nghiêm trọng.

- Các bước tái hiện.

- Kết quả mong đợi và thực tế.

- Commit sửa lỗi.



## 8. Lưu trữ minh chứng



Ảnh chụp kết quả kiểm thử được lưu tại:



`docs/screenshots/`



Báo cáo kết quả kiểm thử được lưu tại:



`docs/test-report.md`



## 9. Tiêu chí hoàn thành



- Các Test Case trong kế hoạch đã được thực hiện.

- Kết quả PASS/FAIL được ghi nhận trung thực.

- Có ảnh chụp minh chứng tương ứng.

- Các lỗi phát hiện được ghi nhận trong Bug Log.

- Có thể chạy lại bộ kiểm thử bằng một lệnh thống nhất.
## 10. Danh sách Test Case

Bộ kiểm thử gồm 18 Test Case, tập trung vào ba nhóm chức năng: quản lý khách hàng, quản lý thiết bị và xử lý thời gian SLA trong luồng tiếp nhận bảo hành.

### 10.1. Phân nhóm Test Case

| Nhóm kiểm thử | Test Case | Mục đích |
|---|---|---|
| Luồng đúng | TC-01, TC-06, TC-09, TC-10, TC-11, TC-12 | Kiểm tra nghiệp vụ và quy tắc tính SLA |
| Giá trị biên | TC-02, TC-03, TC-13, TC-14 | Kiểm tra giới hạn số điện thoại, thời gian làm việc và số giờ SLA |
| Dữ liệu sai | TC-04, TC-05, TC-07, TC-08, TC-16 | Kiểm tra dữ liệu thiếu hoặc không hợp lệ |
| Bảo mật/chất lượng dữ liệu | TC-15, TC-17, TC-18 | Kiểm tra số điện thoại trùng, SQL Injection và truy vấn SQL tham số |
| Tái lập | Chạy lại toàn bộ 18 Test Case | Xác nhận kết quả kiểm thử ổn định |

### 10.2. Kiểm thử SLA

Sáu Test Case kiểm thử SLA bao gồm:

- TC-09: Kiểm tra cấu hình mức ưu tiên SLA.
- TC-10: Kiểm tra tính giờ trong buổi sáng.
- TC-11: Kiểm tra bỏ qua giờ nghỉ trưa.
- TC-12: Kiểm tra bỏ qua ngày cuối tuần.
- TC-13: Kiểm tra thời điểm bắt đầu trước giờ làm việc.
- TC-14: Kiểm tra trường hợp số giờ bằng 0.

### 10.3. Kết quả thực hiện ban đầu

Theo kết quả chạy kiểm thử ngày 07/11/2026:

- Tổng số Test Case: 18.
- Số Test Case PASS: 18.
- Số Test Case FAIL: 0.
- Bộ kiểm thử gồm 12 Test Case quản lý khách hàng, thiết bị và 6 Test Case SLA.
- Toàn bộ bộ kiểm thử đã được thực thi bằng lệnh `python -m pytest -v`.

Kết quả chi tiết và ảnh chụp minh chứng được trình bày trong `docs/test-report.md` và thư mục `docs/screenshots/`.

Lưu ý: Kết quả được ghi nhận theo lần chạy thực tế, không suy diễn kết quả cho các Test Case chưa thực hiện.