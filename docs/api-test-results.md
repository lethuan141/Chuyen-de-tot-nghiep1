\# API Test Results – Smart CRM Mekong Mobile



\## 1. Mục tiêu kiểm thử



Kiểm tra các API tiếp nhận bảo hành nhằm xác minh chức năng tra cứu khách hàng, tra cứu thiết bị, tạo khách hàng và tạo phiếu bảo hành. Đồng thời kiểm tra các trường hợp dữ liệu không hợp lệ và các điều kiện nghiệp vụ.



\## 2. Môi trường kiểm thử



\- Framework: FastAPI

\- Công cụ kiểm thử: Swagger UI

\- Địa chỉ API: `http://127.0.0.1:8000`

\- Kết quả được ghi nhận qua HTTP status code, response body và ảnh chụp màn hình.



\## 3. Bảng kết quả kiểm thử



| ID | API | Trường hợp kiểm thử | Kết quả thực tế | Đánh giá |

|---|---|---|---|---|

| TC01 | POST `/api/tickets` | Tạo phiếu bảo hành hợp lệ | HTTP 201 | Đạt |

| TC02 | POST `/api/customers` | Tạo khách hàng hợp lệ | HTTP 201 | Đạt |

| TC03 | GET `/api/devices` | Tra cứu thiết bị tồn tại | HTTP 200 | Đạt |

| TC04 | POST `/api/customers` | Tạo khách hàng với số điện thoại trùng | HTTP 400 | Đạt |

| TC05 | GET `/api/devices` | Tra cứu thiết bị không tồn tại | HTTP 404 | Đạt |

| TC06 | POST `/api/tickets` | Tạo phiếu với khách hàng không tồn tại | HTTP 400 | Đạt |

| TC07 | POST `/api/tickets` | Thiết bị không thuộc khách hàng được chọn | HTTP 400 | Đạt |

| TC08 | POST `/api/tickets` | Sử dụng mức ưu tiên không hợp lệ | HTTP 400 | Đạt |

| TC09 | POST `/api/tickets` | Bỏ trống trường `priority` | HTTP 422 | Đạt |

| TC10 | GET `/api/customers` | Tra cứu khách hàng theo số điện thoại | HTTP 200 | Đạt |



\## 4. Bằng chứng kiểm thử



Ảnh chụp màn hình được lưu trong thư mục `docs/evidence/`:



\- `POST\_tickets\_201.jpg`

\- `POST\_customers\_201.png`

\- `GET\_devices\_200.png`

\- `POST\_customers\_duplicate\_400.png`

\- `GET\_devices\_not\_found\_404.png`

\- `POST\_tickets\_invalid\_customer\_400.png`

\- `POST\_tickets\_wrong\_customer\_device\_400.png`

\- `POST\_tickets\_invalid\_priority\_400.png`

\- `POST\_tickets\_missing\_priority\_422.png`

\- `GET\_customers\_200.png`



\## 5. Kết luận



Đã thực hiện 10 trường hợp kiểm thử API cơ bản, bao gồm các trường hợp thành công, dữ liệu trùng lặp, dữ liệu không tồn tại, vi phạm quan hệ khách hàng – thiết bị, mức ưu tiên không hợp lệ và thiếu trường bắt buộc.



Các kết quả thực tế phù hợp với kết quả mong đợi của từng trường hợp kiểm thử. Bộ kiểm thử này là cơ sở để tiếp tục rà soát yêu cầu nghiệp vụ, hợp đồng API và tài liệu thiết kế của hệ thống.



