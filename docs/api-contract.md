# API Contract – Tiếp nhận và phân loại yêu cầu bảo hành

## 1. Danh sách endpoints

| Method | Endpoint | Mục đích |
|---|---|---|
| GET | `/api/customers?phone={phone}` | Tra cứu khách hàng bằng số điện thoại |
| POST | `/api/warranty-requests` | Tạo yêu cầu bảo hành |
| GET | `/api/warranty-requests/{id}` | Xem chi tiết yêu cầu bảo hành |

## 2. GET /api/customers

### Request
```http
GET /api/customers?phone=0901234567
```

### Response 200
```json
{
  "customerId": "CUS001",
  "fullName": "Nguyen Van A",
  "phone": "0901234567"
}
```

### Response lỗi
```json
{
  "code": "CUSTOMER_NOT_FOUND",
  "message": "Không tìm thấy khách hàng"
}
```

## 3. POST /api/warranty-requests

### Request
```json
{
  "customerId": "CUS001",
  "deviceId": "DEV001",
  "faultDescription": "Thiết bị không lên nguồn",
  "incidentType": "POWER",
  "priority": "HIGH"
}
```

### Response 201
```json
{
  "requestId": "WR001",
  "status": "RECEIVED",
  "commitmentDeadline": "2026-10-10T17:00:00"
}
```

### Response lỗi
```json
{
  "code": "VALIDATION_ERROR",
  "message": "Thiếu thông tin bắt buộc"
}
```

## 4. GET /api/warranty-requests/{id}

### Response 200
```json
{
  "requestId": "WR001",
  "customerId": "CUS001",
  "deviceId": "DEV001",
  "faultDescription": "Thiết bị không lên nguồn",
  "incidentType": "POWER",
  "priority": "HIGH",
  "status": "RECEIVED",
  "commitmentDeadline": "2026-10-10T17:00:00"
}
```

## 5. Mã trạng thái HTTP

| HTTP | Ý nghĩa |
|---|---|
| 200 | Thành công |
| 201 | Tạo dữ liệu thành công |
| 400 | Request không hợp lệ |
| 401 | Chưa xác thực |
| 403 | Không có quyền |
| 404 | Không tìm thấy dữ liệu |
| 500 | Lỗi máy chủ |

## 6. Validation

| Trường | Kiểu | Bắt buộc | Quy tắc |
|---|---|---|---|
| customerId | string | Có | Không rỗng, phải tồn tại |
| deviceId | string | Có | Không rỗng, phải tồn tại |
| faultDescription | string | Có | 5–500 ký tự |
| incidentType | string | Có | Phải thuộc danh sách loại sự cố |
| priority | string | Có | LOW/MEDIUM/HIGH |
| phone | string | Có | 10–11 chữ số |
