# API Contract – Smart CRM Mekong Mobile

## 1. Mục đích

Tài liệu API Contract mô tả các giao diện API đề xuất phục vụ luồng nghiệp vụ L2 – Tiếp nhận và phân loại yêu cầu bảo hành của hệ thống Smart CRM – Mekong Mobile.

Các API hỗ trợ nhân viên tiếp nhận thực hiện những chức năng chính:

- Tra cứu khách hàng theo số điện thoại.
- Tạo hồ sơ khách hàng mới.
- Tra cứu thiết bị theo Serial/IMEI.
- Tiếp nhận thông tin sự cố và tạo phiếu bảo hành.

API Contract được xây dựng dựa trên yêu cầu nghiệp vụ, User Story, Use Case và Functional Requirement trong tài liệu SRS.

**Lưu ý:** Các endpoint trong tài liệu là đặc tả API đề xuất phục vụ phân tích và thiết kế phần mềm trong Track SE, không khẳng định các API đã được triển khai trong hệ thống thực tế.

## 2. Quy ước chung

- **Base URL:** `/api`
- **Định dạng dữ liệu:** JSON
- **Encoding:** UTF-8
- **Content-Type:** `application/json` đối với request có body.
- **Phương thức HTTP:** GET dùng để tra cứu dữ liệu; POST dùng để tạo tài nguyên mới.

### 2.1. Danh sách API

| Method | Endpoint | Chức năng | Actor |
|---|---|---|---|
| GET | `/api/customers?phone={phone}` | Tra cứu khách hàng theo số điện thoại | Nhân viên tiếp nhận |
| POST | `/api/customers` | Tạo hồ sơ khách hàng | Nhân viên tiếp nhận |
| GET | `/api/devices?serial_no={serial_no}` | Tra cứu thiết bị theo Serial/IMEI | Nhân viên tiếp nhận |
| POST | `/api/tickets` | Tạo phiếu bảo hành | Nhân viên tiếp nhận |

## 3. API 01 – Tra cứu khách hàng

**Endpoint:** `GET /api/customers?phone={phone}`

**Mục đích:** Tìm kiếm hồ sơ khách hàng bằng số điện thoại để phục vụ quá trình tiếp nhận yêu cầu bảo hành.

### Request

Ví dụ:

`GET /api/customers?phone=0901234567`

| Tham số | Kiểu dữ liệu | Bắt buộc | Quy tắc kiểm tra |
|---|---|---|---|
| phone | string | Có | Không được rỗng; phải đúng định dạng số điện thoại được hệ thống hỗ trợ |

### Response – Thành công (200)

```json
{
  "customer_id": "CUS001",
  "customer_name": "Nguyễn Văn A",
  "phone": "0901234567"
}
```

### Response – Không tìm thấy (404)

```json
{
  "message": "Customer not found"
}
```

### HTTP Status

| Status | Ý nghĩa |
|---|---|
| 200 | Tra cứu khách hàng thành công |
| 400 | Số điện thoại không hợp lệ |
| 404 | Không tìm thấy khách hàng |
| 500 | Lỗi hệ thống |

## 4. API 02 – Tạo hồ sơ khách hàng

**Endpoint:** `POST /api/customers`

**Mục đích:** Tạo hồ sơ khách hàng mới khi số điện thoại tra cứu chưa có trong hệ thống.

### Request

Header:

`Content-Type: application/json`

Request Body:

```json
{
  "customer_name": "Nguyễn Văn A",
  "phone": "0901234567"
}
```

### Validation

| Trường | Kiểu dữ liệu | Bắt buộc | Quy tắc kiểm tra |
|---|---|---|---|
| customer_name | string | Có | Không được rỗng |
| phone | string | Có | Không được rỗng, đúng định dạng và không trùng số điện thoại khách hàng đã tồn tại |

### Response – Thành công (201)

```json
{
  "customer_id": "CUS001",
  "customer_name": "Nguyễn Văn A",
  "phone": "0901234567"
}
```

### HTTP Status

| Status | Ý nghĩa |
|---|---|
| 201 | Tạo hồ sơ khách hàng thành công |
| 400 | Dữ liệu đầu vào không hợp lệ |
| 409 | Số điện thoại đã tồn tại |
| 500 | Lỗi hệ thống |

## 5. API 03 – Tra cứu thiết bị

**Endpoint:** `GET /api/devices?serial_no={serial_no}`

**Mục đích:** Tra cứu thông tin thiết bị dựa trên Serial/IMEI để xác định thiết bị khách hàng yêu cầu bảo hành.

### Request

Ví dụ:

`GET /api/devices?serial_no=IMEI123456789`

### Query Parameters

| Tham số | Kiểu dữ liệu | Bắt buộc | Quy tắc kiểm tra |
|---|---|---|---|
| serial_no | string | Có | Không được rỗng; phải có định dạng phù hợp với loại thiết bị được hỗ trợ |

### Response – Thành công (200)

```json
{
  "device_id": "DEV001",
  "serial_no": "IMEI123456789",
  "customer_id": "CUS001",
  "purchase_date": "2026-01-15"
}
```

### Response – Không tìm thấy (404)

```json
{
  "message": "Device not found"
}
```

### HTTP Status

| Status | Ý nghĩa |
|---|---|
| 200 | Tra cứu thiết bị thành công |
| 400 | Serial/IMEI không hợp lệ |
| 404 | Không tìm thấy thiết bị |
| 500 | Lỗi hệ thống |

## 6. API 04 – Tạo phiếu bảo hành

**Endpoint:** `POST /api/tickets`

**Mục đích:** Tiếp nhận thông tin sự cố, phân loại nhóm sự cố, xác định mức ưu tiên và tạo phiếu bảo hành cho khách hàng.

### Request

Header:

`Content-Type: application/json`

Request Body:

```json
{
  "customer_id": "CUS001",
  "device_id": "DEV001",
  "issue_description": "Thiết bị không lên nguồn",
  "issue_category": "POWER",
  "priority": "CAO"
}
```

### Validation

| Trường | Kiểu dữ liệu | Bắt buộc | Quy tắc kiểm tra |
|---|---|---|---|
| customer_id | string | Có | Phải tồn tại trong hệ thống |
| device_id | string | Có | Phải tồn tại và thuộc khách hàng tương ứng |
| issue_description | string | Có | Không được rỗng |
| issue_category | string | Có | Phải thuộc nhóm sự cố được hệ thống hỗ trợ |
| priority | string | Có | Chỉ nhận `CAO`, `TRUNG_BINH` hoặc `THAP` |

### Response – Thành công (201)

```json
{
  "ticket_id": "TIC001",
  "customer_id": "CUS001",
  "device_id": "DEV001",
  "issue_category": "POWER",
  "priority": "CAO",
  "status": "MỚI",
  "commitment_deadline": "2026-10-07T17:00:00"
}
```

Trong đó:

- `ticket_id`: Mã phiếu bảo hành được hệ thống tạo.
- `issue_category`: Nhóm sự cố đã được xác định.
- `priority`: Mức độ ưu tiên của yêu cầu.
- `status`: Trạng thái ban đầu của phiếu.
- `commitment_deadline`: Hạn cam kết xử lý được hệ thống tính toán.

### HTTP Status

| Status | Ý nghĩa |
|---|---|
| 201 | Tạo phiếu bảo hành thành công |
| 400 | Dữ liệu đầu vào không hợp lệ |
| 404 | Không tìm thấy khách hàng hoặc thiết bị |
| 409 | Thiết bị không thuộc khách hàng hoặc dữ liệu có xung đột |
| 500 | Lỗi hệ thống |

## 7. Quy tắc nghiệp vụ liên quan đến API

### 7.1. Số điện thoại khách hàng

- Số điện thoại phải được chuẩn hóa trước khi lưu trữ và tra cứu.
- Một số điện thoại chỉ được liên kết với một hồ sơ khách hàng.
- Khi tạo hồ sơ mới, hệ thống phải kiểm tra số điện thoại đã tồn tại hay chưa.

### 7.2. Thông tin thiết bị

- Thiết bị được tra cứu thông qua Serial/IMEI.
- Thiết bị phải được xác định chính xác trước khi tạo phiếu bảo hành.
- Hệ thống phải kiểm tra mối liên hệ giữa thiết bị và khách hàng trước khi tiếp nhận yêu cầu.

### 7.3. Phân loại sự cố và mức ưu tiên

Hệ thống tiếp nhận mô tả lỗi, xác định nhóm sự cố và mức ưu tiên phù hợp với quy tắc nghiệp vụ.

Ba mức ưu tiên được sử dụng:

| Mức ưu tiên | Giá trị API |
|---|---|
| Cao | `CAO` |
| Trung bình | `TRUNG_BINH` |
| Thấp | `THAP` |

Các giá trị nhóm sự cố phải thuộc danh mục được hệ thống hỗ trợ. Ví dụ, `POWER` có thể được sử dụng cho nhóm sự cố liên quan đến nguồn điện.

### 7.4. Tính hạn cam kết

Hạn cam kết được xác định dựa trên mức ưu tiên của phiếu bảo hành.

| Mức ưu tiên | Thời hạn xử lý dự kiến |
|---|---|
| CAO | 24 giờ |
| TRUNG_BINH | 72 giờ |
| THAP | 120 giờ |

Theo quy tắc nghiệp vụ của đề tài, ngày làm việc được tính từ thứ Hai đến thứ Bảy.

Cần thống nhất trong SRS và phần triển khai rằng các thời hạn trên được tính theo giờ thực tế hay giờ làm việc. API chỉ trả về `commitment_deadline` sau khi hệ thống áp dụng quy tắc tính hạn đã được thống nhất.

### 7.5. Trường hợp không có ngày mua

Nếu thiết bị chưa có thông tin ngày mua, tình trạng bảo hành được đánh dấu là chưa xác minh. Trường hợp này cần được chuyển đến quản lý trung tâm để kiểm tra hoặc phê duyệt theo quy trình nghiệp vụ.

### 7.6. Lịch sử trạng thái phiếu

Mỗi lần trạng thái phiếu bảo hành thay đổi, hệ thống cần ghi nhận lịch sử để phục vụ theo dõi và truy vết.

Thông tin lịch sử có thể bao gồm mã phiếu, trạng thái trước đó, trạng thái mới, thời điểm thay đổi và người thực hiện. Tên bảng lưu trữ cụ thể, chẳng hạn `ticket_status_log`, cần thống nhất với thiết kế cơ sở dữ liệu.

## 8. Tổng hợp HTTP Status Code

| Status | Ý nghĩa | Trường hợp sử dụng |
|---|---|---|
| 200 | OK | Tra cứu dữ liệu thành công |
| 201 | Created | Tạo khách hàng hoặc phiếu bảo hành thành công |
| 400 | Bad Request | Thiếu dữ liệu hoặc dữ liệu không hợp lệ |
| 404 | Not Found | Không tìm thấy khách hàng hoặc thiết bị |
| 409 | Conflict | Trùng số điện thoại hoặc dữ liệu có xung đột |
| 500 | Internal Server Error | Lỗi xử lý phía máy chủ |

Các response lỗi cần cung cấp thông báo phù hợp để phía giao diện có thể hiển thị cho nhân viên tiếp nhận.

## 9. Traceability – Liên kết với yêu cầu

| API | User Story | Use Case | Functional Requirement |
|---|---|---|---|
| GET `/api/customers?phone={phone}` | US01 | UC01 – Tra cứu khách hàng | FR01 |
| POST `/api/customers` | US02 | UC02 – Tạo hồ sơ khách hàng | FR02 |
| GET `/api/devices?serial_no={serial_no}` | US03 | UC03 – Ghi nhận thiết bị | FR03 |
| POST `/api/tickets` | US05, US06, US07, US08 | UC05, UC06, UC07, UC08 | FR05, FR06, FR07, FR08 |

API tạo phiếu bảo hành hỗ trợ nhiều bước nghiệp vụ gồm tạo phiếu, ghi nhận mô tả lỗi, phân loại nhóm sự cố và xác định mức ưu tiên. Việc tính hạn cam kết tương ứng với UC09 và FR09 cần được thể hiện trong luồng xử lý của API này hoặc một thành phần nghiệp vụ liên quan.

## 10. Giới hạn của API Contract

- Các endpoint được đề xuất dựa trên phạm vi luồng L2, chưa khẳng định đã được triển khai.
- Tài liệu tập trung vào tra cứu khách hàng, tạo hồ sơ khách hàng, tra cứu thiết bị và tạo phiếu bảo hành.
- Các API quản lý sửa chữa, linh kiện, thanh toán và doanh thu nằm ngoài phạm vi của luồng L2.
- Các quy tắc xác thực, phân loại sự cố, tính hạn cam kết và ghi nhận lịch sử cần được đối chiếu với SRS, Use Case và thiết kế cơ sở dữ liệu trước khi triển khai.