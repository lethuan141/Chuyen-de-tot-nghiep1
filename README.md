# Smart CRM – Mekong Mobile

## 1. Giới thiệu đề tài

Đề tài tập trung phân tích **Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành** trong hệ thống Smart CRM của Mekong Mobile.

Mục tiêu của bài thực hành là phân tích yêu cầu nghiệp vụ và chuyển đổi thành các tài liệu đặc tả phần mềm phục vụ quá trình thiết kế và phát triển hệ thống, bao gồm SRS, User Story, Use Case, Business Flow và API Contract.

Phạm vi nghiệp vụ chính:

- Tra cứu thông tin khách hàng.
- Tạo hồ sơ khách hàng mới.
- Ghi nhận thông tin thiết bị.
- Kiểm tra tình trạng bảo hành.
- Tạo phiếu bảo hành.
- Ghi nhận mô tả lỗi.
- Phân loại nhóm sự cố.
- Xác định mức độ ưu tiên.
- Sinh hạn cam kết xử lý.

## ## 2. Môi trường thực hiện

Dự án sử dụng Python, FastAPI và MySQL để xây dựng API phục vụ luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành.

### 2.1. Yêu cầu môi trường

- **Hệ điều hành:** Windows 10/11.
- **Ngôn ngữ lập trình:** Python 3.11.
- **Framework backend:** FastAPI 0.115.6.
- **ASGI server:** Uvicorn 0.34.0.
- **Cơ sở dữ liệu:** MySQL Server 8.0 trở lên.
- **Thư viện kết nối MySQL:** PyMySQL.
- **Quản lý biến môi trường:** python-dotenv.
- **Quản lý mã nguồn:** Git và GitHub.
- **Công cụ kiểm thử API:** Swagger UI tại `/docs`.
- **Công cụ chỉnh sửa:** Visual Studio Code hoặc trình soạn thảo tương đương.

### 2.2. Cài đặt và khởi chạy

Cài đặt các thư viện cần thiết:

```bash
pip install fastapi==0.115.6 uvicorn==0.34.0 PyMySQL python-dotenv
```

Tạo file `.env` tại thư mục gốc dự án và cấu hình thông tin kết nối MySQL theo mẫu trong `.env.example`.

Đảm bảo MySQL đang hoạt động và cơ sở dữ liệu `smart_crm_mekong_mobile` đã được tạo. Có thể sử dụng các script SQL trong `migrations/` và `seed/` để tạo bảng và nạp dữ liệu mẫu khi cần.

Khởi chạy API:

```bash
python -m uvicorn src.main:app --reload
```

Truy cập Swagger UI:

```text
http://127.0.0.1:8000/docs
```

**Lưu ý:** Không đưa file `.env`, mật khẩu cơ sở dữ liệu hoặc khóa bí mật lên GitHub. Chỉ sử dụng `.env.example` để cung cấp cấu hình mẫu.
Không yêu cầu khởi chạy server hoặc kết nối cơ sở dữ liệu để đọc và kiểm tra các tài liệu phân tích.

## ## 3. Cấu trúc repository

```text
Chuyen-de-tot-nghiep1/
├── Diagram/
│   ├── business_flow_L2.drawio
│   ├── Database.drawio
│   ├── MÔ HÌNH.drawio
│   ├── use_case_L2.drawio
│   └── Wireframe1.drawio
│
├── docs/
│   ├── evidence/
│   ├── ai-disclosure.md
│   ├── api-contract.md
│   ├── api-test-results.md
│   ├── srs.md
│   ├── thay-doi-thiet-ke.md
│   └── usecase.drawio
│
├── migrations/
│   └── 001_create_tables.sql
│
├── seed/
│   └── 001_seed_data.sql
│
├── src/
│   ├── routes/
│   ├── services/
│   ├── repositories/
│   ├── db.py
│   └── main.py
│
├── .env.example
├── .gitignore
└── README.md
```

*Lưu ý: Cây thư mục trên thể hiện các thành phần chính. Tên và số lượng tệp cần được đối chiếu với repository thực tế.*

**Chức năng các thư mục:**

- `src/routes/`: Tiếp nhận và định tuyến các yêu cầu HTTP.
- `src/services/`: Xử lý logic nghiệp vụ.
- `src/repositories/`: Thực hiện truy vấn và thao tác dữ liệu.
- `migrations/`: Lưu các script SQL khởi tạo hoặc thay đổi cấu trúc cơ sở dữ liệu.
- `seed/`: Lưu script tạo dữ liệu mẫu.
- `docs/`: Lưu tài liệu phân tích, đặc tả, API Contract, báo cáo thay đổi thiết kế và kết quả kiểm thử.
- `docs/evidence/`: Lưu ảnh minh chứng kiểm thử API.
- `Diagram/`: Lưu các sơ đồ nghiệp vụ, cơ sở dữ liệu và giao diện.
- `.env.example`: Cung cấp mẫu biến môi trường.
- `.gitignore`: Loại trừ các tệp không nên đưa vào Git.
- `README.md`: Giới thiệu đề tài, môi trường và trạng thái thực hiện.
## 4. Danh sách tài liệu

| Tài liệu | Nội dung |
|---|---|
| `docs/srs.md` | Đặc tả yêu cầu phần mềm, User Story, Acceptance Criteria, FR, NFR và Traceability. |
| `docs/usecase.drawio` | Sơ đồ Use Case được lưu trong thư mục tài liệu. |
| `docs/api-contract.md` | Mô tả các API đề xuất cho Track SE. |
| `docs/ai-disclosure.md` | Công khai mục đích và phạm vi sử dụng công cụ AI trong quá trình thực hiện. |
| `diagrams/business_flow_L2.drawio` | Sơ đồ luồng nghiệp vụ L2 – Tiếp nhận và phân loại yêu cầu bảo hành. |
| `diagrams/use_case_L2.drawio` | Sơ đồ Use Case tổng quan của luồng L2. |

Các tệp `.drawio` có thể được mở và chỉnh sửa bằng draw.io Desktop hoặc draw.io trên trình duyệt.

## 5. Luồng nghiệp vụ được phân tích

**Mã luồng:** L2

**Tên luồng:** Tiếp nhận và phân loại yêu cầu bảo hành.

### 5.1. Actor

- **Nhân viên tiếp nhận:** Tiếp nhận thông tin khách hàng, thiết bị và yêu cầu bảo hành.
- **Quản lý trung tâm:** Hỗ trợ xác minh tình trạng bảo hành trong các trường hợp cần kiểm tra thêm.
- **Hệ thống Smart CRM:** Kiểm tra dữ liệu, lưu thông tin phiếu và xác định hạn cam kết theo quy tắc nghiệp vụ.

### 5.2. Danh sách Use Case

| Mã | Tên Use Case |
|---|---|
| UC01 | Tra cứu khách hàng |
| UC02 | Tạo hồ sơ khách hàng |
| UC03 | Ghi nhận thiết bị |
| UC04 | Kiểm tra tình trạng bảo hành |
| UC05 | Tạo phiếu bảo hành (Đặc tả) |
| UC06 | Ghi nhận mô tả lỗi |
| UC07 | Phân loại nhóm sự cố |
| UC08 | Xác định mức ưu tiên |
| UC09 | Sinh hạn cam kết |

### 5.3. Mô tả khái quát quy trình

1. Nhân viên tiếp nhận tra cứu thông tin khách hàng bằng số điện thoại.
2. Nếu chưa có hồ sơ phù hợp, nhân viên tạo hồ sơ khách hàng mới.
3. Nhân viên tra cứu và ghi nhận thiết bị bằng serial hoặc IMEI.
4. Hệ thống kiểm tra tình trạng bảo hành; trường hợp chưa đủ thông tin được chuyển xác minh theo quy trình.
5. Nhân viên ghi nhận mô tả lỗi của khách hàng.
6. Nhân viên phân loại nhóm sự cố và xác định mức ưu tiên.
7. Nhân viên tạo phiếu bảo hành với các thông tin bắt buộc hợp lệ.
8. Hệ thống sinh mã phiếu, xác định hạn cam kết theo quy tắc nghiệp vụ và lưu thông tin cần thiết.

## ## 6. Trạng thái tiến độ hiện tại

Dự án đã chuyển từ giai đoạn phân tích và đặc tả yêu cầu sang giai đoạn hiện thực backend ban đầu cho luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành.

### 6.1. Cấu trúc mã nguồn

Đã xây dựng cấu trúc phân lớp trong `src/`, gồm:

- `src/routes/`: Tiếp nhận và xử lý các yêu cầu HTTP.
- `src/services/`: Xử lý logic nghiệp vụ.
- `src/repositories/`: Truy vấn và ghi dữ liệu vào MySQL.
- `src/db.py`: Thiết lập kết nối cơ sở dữ liệu.
- `src/main.py`: Khởi tạo ứng dụng FastAPI và đăng ký các router.

### ### 6.2. Chức năng đã hiện thực và kiểm thử

Các chức năng backend ban đầu đã được triển khai cho luồng L2, bao gồm:

- Tra cứu khách hàng theo số điện thoại.
- Tạo hồ sơ khách hàng mới và phát hiện số điện thoại trùng.
- Tra cứu thiết bị theo Serial/IMEI.
- Tạo phiếu bảo hành với mã phiếu tự động.
- Xác định hạn cam kết xử lý theo quy tắc SLA.
- Kiểm tra sự tồn tại của khách hàng và mối liên hệ giữa khách hàng với thiết bị trước khi tạo phiếu.

Các API đã được kiểm thử trên Swagger UI với các trường hợp thành công và ngoại lệ:

- Tạo khách hàng thành công: HTTP 201.
- Tra cứu khách hàng và thiết bị thành công: HTTP 200.
- Tạo phiếu bảo hành thành công: HTTP 201.
- Số điện thoại bị trùng: HTTP 400.
- Không tìm thấy thiết bị: HTTP 404.
- Khách hàng không hợp lệ hoặc thiết bị không thuộc khách hàng: HTTP 400.
- Mức ưu tiên không hợp lệ: HTTP 400.
- Thiếu trường bắt buộc: HTTP 422.

Kết quả và ảnh minh chứng được lưu trong `docs/api-test-results.md` và `docs/evidence/`. Mã nguồn cũng đã được kiểm tra cú pháp bằng `python -m compileall src`.

**Lưu ý:** Các chức năng đã kiểm thử nêu trên chưa đồng nghĩa với việc toàn bộ CRUD của entity chính đã hoàn thành.

### 6.3. Cơ sở dữ liệu

Đã có các script:

- `migrations/001_create_tables.sql`: Khởi tạo các bảng khách hàng, nhân viên, thiết bị, nhóm sự cố, mức ưu tiên, phiếu bảo hành và lịch sử trạng thái.
- `seed/001_seed_data.sql`: Nạp dữ liệu mẫu cho nhân viên, nhóm sự cố, mức ưu tiên, khách hàng và thiết bị.

Cần tiếp tục rà soát tính nhất quán giữa migration, dữ liệu mẫu và DDL đã thống nhất trong BT1.

### ### 6.4. Tài liệu và cấu hình

- Đã có tài liệu SRS, API Contract, Use Case và AI Disclosure.
- Đã tạo `docs/thay-doi-thiet-ke.md` để ghi nhận các thay đổi thiết kế sau phản hồi BT1.
- Đã tạo `docs/api-test-results.md` để tổng hợp các trường hợp kiểm thử API.
- Đã lưu ảnh minh chứng kiểm thử trong `docs/evidence/`.
- Đã có `.gitignore` và `.env.example`; cần bảo đảm file `.env`, thông tin đăng nhập và các dữ liệu nhạy cảm không được đưa lên GitHub.
- Tiếp tục đối chiếu migration và seed dữ liệu với thiết kế cơ sở dữ liệu đã thống nhất trong BT1.

### ### 6.5. Công việc tiếp theo

- Hoàn thiện và kiểm thử các thao tác CRUD cho entity chính theo yêu cầu Track SE.
- Rà soát tính nhất quán giữa migration, seed dữ liệu và DDL đã thống nhất trong BT1.
- Kiểm tra `.gitignore` và `.env.example`, bảo đảm không đưa thông tin nhạy cảm lên GitHub.
- Bổ sung kiểm thử cho các trường hợp nghiệp vụ chưa được bao phủ.
- Tiếp tục cập nhật tài liệu khi có thay đổi về thiết kế hoặc triển khai.

## 7. Phạm vi và giới hạn

Repository hiện tập trung vào phân tích nghiệp vụ, đặc tả yêu cầu và thiết kế ở mức tài liệu. Các API trong `docs/api-contract.md` là đề xuất phục vụ thiết kế, chưa khẳng định đã được triển khai hoặc kết nối với hệ thống thực tế của Mekong Mobile.

Việc triển khai giao diện, backend, cơ sở dữ liệu và kiểm thử tích hợp có thể được thực hiện ở giai đoạn tiếp theo nếu nằm trong phạm vi môn học.

## 8. Kết luận

Repository **Smart CRM – Mekong Mobile** là sản phẩm phân tích yêu cầu cho Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành. Các tài liệu được tổ chức nhằm thể hiện mối liên hệ giữa nghiệp vụ, User Story, Use Case, yêu cầu chức năng, yêu cầu phi chức năng và API Contract.

Đây là cơ sở để tiếp tục thiết kế hệ thống, xây dựng các thành phần phần mềm và kiểm thử yêu cầu trong những giai đoạn tiếp theo.