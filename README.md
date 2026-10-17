# Smart CRM – Mekong Mobile

## 1. Giới thiệu đề tài

Đề tài tập trung phân tích và triển khai bước đầu **Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành** trong hệ thống Smart CRM của Mekong Mobile.

Mục tiêu là phân tích yêu cầu nghiệp vụ và chuyển đổi thành các tài liệu đặc tả phần mềm phục vụ thiết kế, phát triển và kiểm thử hệ thống, bao gồm SRS, User Story, Use Case, Business Flow và API Contract.

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

## 2. Môi trường thực hiện

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

Đảm bảo MySQL đang hoạt động và cơ sở dữ liệu `smart_crm_mekong_mobile` đã được tạo. Trước khi chạy ứng dụng, kiểm tra các script SQL trong `migrations/` và `seed/`, sau đó thực hiện tạo bảng và nạp dữ liệu mẫu theo cấu trúc dự án.

Khởi chạy API:

```bash
python -m uvicorn src.main:app --reload
```

Truy cập Swagger UI:

```text
http://127.0.0.1:8000/docs
```

**Lưu ý bảo mật:** Không đưa file `.env`, mật khẩu cơ sở dữ liệu hoặc khóa bí mật lên GitHub. Chỉ sử dụng `.env.example` để cung cấp cấu hình mẫu. Không cần khởi chạy server hoặc kết nối cơ sở dữ liệu chỉ để đọc các tài liệu phân tích.

## 3. Cấu trúc repository

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

*Cây thư mục trên mô tả các thành phần chính dự kiến của repository. Cần đối chiếu với các tệp thực tế trong GitHub trước khi chốt tài liệu.*

**Chức năng các thư mục:**

- `src/routes/`: Tiếp nhận và định tuyến các yêu cầu HTTP.
- `src/services/`: Xử lý logic nghiệp vụ.
- `src/repositories/`: Truy vấn và thao tác dữ liệu.
- `migrations/`: Lưu các script SQL khởi tạo hoặc thay đổi cấu trúc cơ sở dữ liệu.
- `seed/`: Lưu script tạo dữ liệu mẫu.
- `docs/`: Lưu tài liệu phân tích, đặc tả, API Contract, nhật ký thay đổi thiết kế và kết quả kiểm thử.
- `docs/evidence/`: Lưu ảnh minh chứng kiểm thử API.
- `Diagram/`: Lưu các sơ đồ nghiệp vụ, cơ sở dữ liệu, Use Case và giao diện.
- `.env.example`: Cung cấp mẫu biến môi trường.
- `.gitignore`: Loại trừ các tệp không nên đưa vào Git.
- `README.md`: Giới thiệu đề tài, môi trường và trạng thái thực hiện.

## 4. Danh sách tài liệu

| Tài liệu | Nội dung |
|---|---|
| `docs/srs.md` | Đặc tả yêu cầu phần mềm, User Story, Acceptance Criteria, FR, NFR và Traceability. |
| `docs/usecase.drawio` | Sơ đồ Use Case được lưu trong thư mục tài liệu. |
| `docs/api-contract.md` | Mô tả hợp đồng API của dự án. |
| `docs/api-test-results.md` | Tổng hợp kết quả kiểm thử API. |
| `docs/ai-disclosure.md` | Công khai mục đích và phạm vi sử dụng công cụ AI trong quá trình thực hiện. |
| `docs/thay-doi-thiet-ke.md` | Nhật ký thay đổi thiết kế và trạng thái thực hiện Buổi 08. |
| `Diagram/business_flow_L2.drawio` | Sơ đồ luồng nghiệp vụ L2. |
| `Diagram/use_case_L2.drawio` | Sơ đồ Use Case tổng quan của luồng L2. |
| `Diagram/Database.drawio` | Sơ đồ cơ sở dữ liệu. |
| `Diagram/MÔ HÌNH.drawio` | Sơ đồ mô hình hệ thống. |
| `Diagram/Wireframe1.drawio` | Sơ đồ phác thảo giao diện. |

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
3. Nhân viên tra cứu và ghi nhận thiết bị bằng Serial hoặc IMEI.
4. Hệ thống kiểm tra tình trạng bảo hành; trường hợp chưa đủ thông tin được chuyển xác minh theo quy trình.
5. Nhân viên ghi nhận mô tả lỗi của khách hàng.
6. Nhân viên phân loại nhóm sự cố và xác định mức ưu tiên.
7. Nhân viên tạo phiếu bảo hành với các thông tin bắt buộc hợp lệ.
8. Hệ thống sinh mã phiếu, xác định hạn cam kết theo quy tắc nghiệp vụ và lưu thông tin cần thiết.

## 6. Trạng thái tiến độ hiện tại

Dự án đã chuyển từ giai đoạn phân tích, đặc tả yêu cầu sang giai đoạn hiện thực và kiểm thử các API backend ban đầu cho luồng L2.

### 6.1. Cấu trúc mã nguồn

Đã tổ chức mã nguồn backend theo kiến trúc phân lớp:

- `src/routes/`: Tiếp nhận và xử lý các yêu cầu HTTP.
- `src/services/`: Xử lý logic nghiệp vụ.
- `src/repositories/`: Truy vấn và ghi dữ liệu.
- `src/db.py`: Thiết lập kết nối cơ sở dữ liệu.
- `src/main.py`: Khởi tạo ứng dụng FastAPI và đăng ký router.

Đã chạy lệnh `python -m compileall src` để kiểm tra cú pháp mã nguồn.

### 6.2. Chức năng đã hiện thực và kiểm thử

Các chức năng backend đã triển khai gồm tra cứu và tạo hồ sơ khách hàng, tra cứu thiết bị, tạo phiếu bảo hành và các thao tác CRUD đối với phiếu bảo hành.

Các thao tác CRUD của phiếu bảo hành đã được kiểm thử trên Swagger UI:

| Thao tác | API | Kết quả kiểm thử |
|---|---|---|
| Tạo phiếu | `POST /api/tickets` | Thành công – HTTP 201 |
| Xem danh sách | `GET /api/tickets` | Thành công – HTTP 200 |
| Xem chi tiết | `GET /api/tickets/{ticket_id}` | Thành công – HTTP 200 |
| Cập nhật phiếu | `PUT /api/tickets/{ticket_id}` | Thành công – HTTP 200 |
| Xóa phiếu kiểm thử | `DELETE /api/tickets/{ticket_id}` | Thành công – HTTP 200 |

Các trường hợp ngoại lệ đã được kiểm tra:

- Truy cập phiếu bảo hành không tồn tại: HTTP 404.
- Một số trường hợp dữ liệu khách hàng, thiết bị hoặc mức ưu tiên không hợp lệ: đã có ảnh minh chứng cho các API tương ứng trong `docs/evidence/`.
- Thiếu trường bắt buộc khi tạo phiếu: HTTP 422.

Kết quả chi tiết được tổng hợp trong `docs/api-test-results.md`. Cần tiếp tục bảo đảm tài liệu kiểm thử và ảnh minh chứng phản ánh đúng những trường hợp đã chạy thực tế.

### 6.3. Cơ sở dữ liệu

Repository có các script dự kiến phục vụ khởi tạo cấu trúc và dữ liệu mẫu:

- `migrations/001_create_tables.sql`: Script tạo các bảng nghiệp vụ.
- `seed/001_seed_data.sql`: Script nạp dữ liệu mẫu.

Cần tiếp tục rà soát cấu trúc bảng, khóa ngoại, ràng buộc dữ liệu và tính nhất quán giữa migration, seed với thiết kế cơ sở dữ liệu đã thống nhất trong BT1 trước khi xác nhận hoàn thành hạng mục này.

### 6.4. Tài liệu, bảo mật và minh chứng

- Đã có tài liệu SRS, API Contract, Use Case và AI Disclosure.
- Đã cập nhật `docs/thay-doi-thiet-ke.md` để ghi nhận các quyết định thiết kế và tiến độ Buổi 08.
- Đã có `docs/api-test-results.md` để tổng hợp các trường hợp kiểm thử API.
- Đã có thư mục `docs/evidence/` chứa ảnh minh chứng cho các API đã kiểm thử.
- Đã kiểm tra `.gitignore` để bỏ qua file `.env` và các tệp không nên đưa vào Git.
- Đã kiểm tra `.env.example`; thông tin mật khẩu trong tệp mẫu sử dụng giá trị giữ chỗ.
- Cần bổ sung ảnh minh chứng cho các thao tác CRUD còn thiếu nếu chưa được lưu đầy đủ.

### 6.5. Git và phiên bản mã nguồn

Đã tạo và đẩy các commit sau lên nhánh `main`:

- **CRUD phiếu bảo hành:** `afc1d29` – `feat: complete warranty ticket CRUD API`.
- **Cập nhật nhật ký thay đổi thiết kế:** `82ea8d3` – `docs: update design change log for lab 08`.

Các commit có thể xem tại:

- [Commit CRUD phiếu bảo hành](https://github.com/lethuan141/Chuyen-de-tot-nghiep1/commit/afc1d29)
- [Commit nhật ký thay đổi thiết kế](https://github.com/lethuan141/Chuyen-de-tot-nghiep1/commit/82ea8d3)

Sau khi push, Git đã báo nhánh `main` đồng bộ với `origin/main` và working tree sạch.

### 6.6. Công việc tiếp theo

- Đối chiếu migration và seed với thiết kế cơ sở dữ liệu BT1.
- Bổ sung ảnh minh chứng CRUD còn thiếu và cập nhật kết quả kiểm thử tương ứng.
- Rà soát README, API Contract và nhật ký thay đổi thiết kế để bảo đảm thông tin nhất quán.
- Kiểm thử bổ sung các trường hợp ngoại lệ và ràng buộc nghiệp vụ.
- Kiểm tra lại cây thư mục và các đường dẫn tài liệu trước khi nộp báo cáo.

## 7. Phạm vi và giới hạn

Repository tập trung vào phân tích nghiệp vụ, đặc tả yêu cầu và triển khai bước đầu các API backend cho Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành.

Các API được mô tả trong `docs/api-contract.md` cần được đối chiếu với mã nguồn thực tế; không mặc định rằng mọi API trong tài liệu đều đã được triển khai. Dự án cũng chưa được khẳng định là đã hoàn thành kiểm thử tích hợp hoặc triển khai trên môi trường vận hành thực tế của Mekong Mobile.

## 8. Kết luận

Repository **Smart CRM – Mekong Mobile** là sản phẩm phân tích yêu cầu và triển khai backend bước đầu cho Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành.

Các tài liệu được tổ chức nhằm thể hiện mối liên hệ giữa nghiệp vụ, User Story, Use Case, yêu cầu chức năng, yêu cầu phi chức năng và API Contract. Việc triển khai CRUD phiếu bảo hành là bước tiếp theo từ đặc tả sang hiện thực, tạo cơ sở để tiếp tục hoàn thiện cơ sở dữ liệu, kiểm thử và các chức năng nghiệp vụ còn lại.