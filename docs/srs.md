# SRS – Hệ thống tiếp nhận và phân loại yêu cầu bảo hành

## 1. Tổng quan

### 1.1. Mục tiêu
Hệ thống hỗ trợ nhân viên tiếp nhận yêu cầu bảo hành, tra cứu khách hàng, ghi nhận thiết bị và lỗi, phân loại sự cố, xác định mức độ ưu tiên và tạo phiếu bảo hành có thời hạn cam kết xử lý.

### 1.2. Phạm vi
Hệ thống tập trung vào quy trình tiếp nhận yêu cầu bảo hành từ lúc tra cứu khách hàng đến khi tạo phiếu bảo hành. Không bao gồm xử lý sửa chữa thực tế, quản lý kho linh kiện và thanh toán.

### 1.3. Thuật ngữ

| Thuật ngữ | Ý nghĩa |
|---|---|
| Khách hàng | Người sở hữu thiết bị yêu cầu bảo hành |
| Nhân viên | Người tiếp nhận và tạo yêu cầu bảo hành |
| Yêu cầu bảo hành | Thông tin yêu cầu được khách hàng gửi đến hệ thống |
| Phiếu bảo hành | Hồ sơ chính thức được tạo sau khi tiếp nhận yêu cầu |
| Loại sự cố | Nhóm phân loại lỗi của thiết bị |
| Mức ưu tiên | Mức độ cần xử lý của yêu cầu |
| Hạn cam kết | Thời điểm dự kiến hoàn tất xử lý |

## 2. Yêu cầu chức năng

| ID | Yêu cầu |
|---|---|
| FR-01 | Hệ thống cho phép nhân viên tra cứu khách hàng bằng số điện thoại. |
| FR-02 | Hệ thống hiển thị thông tin khách hàng phù hợp với số điện thoại tìm kiếm. |
| FR-03 | Hệ thống cho phép nhân viên ghi nhận thiết bị cần bảo hành. |
| FR-04 | Hệ thống cho phép nhân viên nhập mô tả lỗi/sự cố của thiết bị. |
| FR-05 | Hệ thống cho phép nhân viên phân loại nhóm sự cố. |
| FR-06 | Hệ thống cho phép nhân viên xác định mức độ ưu tiên của yêu cầu. |
| FR-07 | Hệ thống cho phép nhân viên tạo phiếu yêu cầu bảo hành. |
| FR-08 | Hệ thống tự động ghi nhận thời gian tiếp nhận và hạn cam kết xử lý. |

## 3. Yêu cầu phi chức năng

| ID | Yêu cầu |
|---|---|
| NFR-01 | Thời gian phản hồi thao tác tra cứu khách hàng không quá 3 giây trong điều kiện hoạt động bình thường. |
| NFR-02 | Các trường bắt buộc phải được kiểm tra trước khi tạo phiếu bảo hành. |
| NFR-03 | Chỉ nhân viên có quyền mới được tạo và cập nhật yêu cầu bảo hành. |
| NFR-04 | Dữ liệu yêu cầu bảo hành phải được lưu trữ nhất quán và không bị mất khi tạo phiếu thành công. |

## 4. Quy tắc nghiệp vụ

- Số điện thoại khách hàng là thông tin dùng để tra cứu khách hàng.
- Không được tạo phiếu nếu chưa xác định khách hàng, thiết bị, mô tả lỗi, loại sự cố và mức ưu tiên.
- Mỗi yêu cầu bảo hành được cấp một mã phiếu duy nhất.
- Hạn cam kết được xác định dựa trên loại sự cố và mức ưu tiên theo quy định của doanh nghiệp.
- Yêu cầu có mức ưu tiên cao phải được xử lý trước yêu cầu có mức ưu tiên thấp hơn.

## 5. Use Case

### UC-01: Tiếp nhận và tạo yêu cầu bảo hành

**Actor chính:** Nhân viên

**Tiền điều kiện:** Nhân viên đã đăng nhập và có quyền tiếp nhận bảo hành.

**Luồng chính:**
1. Nhân viên nhập số điện thoại khách hàng.
2. Hệ thống kiểm tra và hiển thị thông tin khách hàng.
3. Nhân viên chọn khách hàng và nhập/chọn thiết bị.
4. Nhân viên nhập mô tả lỗi.
5. Hệ thống cho phép chọn nhóm sự cố.
6. Nhân viên xác định mức ưu tiên.
7. Hệ thống xác định hạn cam kết.
8. Nhân viên kiểm tra thông tin và chọn tạo phiếu.
9. Hệ thống kiểm tra dữ liệu bắt buộc.
10. Hệ thống tạo mã phiếu và lưu yêu cầu.
11. Hệ thống thông báo tạo phiếu thành công.

**Luồng ngoại lệ:**
- E1: Không tìm thấy khách hàng → hệ thống thông báo và yêu cầu kiểm tra lại số điện thoại.
- E2: Thiếu trường bắt buộc → hệ thống đánh dấu trường thiếu và không cho tạo phiếu.
- E3: Dữ liệu không hợp lệ → hệ thống thông báo lỗi để nhân viên sửa.
- E4: Lỗi lưu dữ liệu → hệ thống thông báo tạo phiếu thất bại và không xác nhận yêu cầu.

## 6. Truy vết yêu cầu

| FR | User Story | Use Case | Kiểm thử dự kiến |
|---|---|---|---|
| FR-01 | US-01: Tra cứu khách hàng bằng SĐT | UC-01 | TC-01 |
| FR-02 | US-01: Xem thông tin khách hàng | UC-01 | TC-02 |
| FR-03 | US-02: Ghi nhận thiết bị bảo hành | UC-01 | TC-03 |
| FR-04 | US-03: Ghi nhận mô tả lỗi | UC-01 | TC-04 |
| FR-05 | US-04: Phân loại sự cố | UC-01 | TC-05 |
| FR-06 | US-05: Xác định mức ưu tiên | UC-01 | TC-06 |
| FR-07 | US-06: Tạo phiếu bảo hành | UC-01 | TC-07 |
| FR-08 | US-06: Ghi nhận hạn cam kết | UC-01 | TC-08 |
| NFR-01 | US-01 | UC-01 | TC-09 |
| NFR-02 | US-06 | UC-01 | TC-10 |
| NFR-03 | US-06 | UC-01 | TC-11 |
| NFR-04 | US-06 | UC-01 | TC-12 |
