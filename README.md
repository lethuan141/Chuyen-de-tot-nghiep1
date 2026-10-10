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

## 2. Môi trường thực hiện

Repository chủ yếu lưu trữ tài liệu phân tích và đặc tả yêu cầu phần mềm trong khuôn khổ Buổi 04. Vì vậy, bài thực hành không yêu cầu triển khai backend, frontend hoặc cơ sở dữ liệu thực tế.

Môi trường đề xuất:

- **Hệ điều hành:** Windows 10/11.
- **Quản lý mã nguồn:** Git và GitHub.
- **Chỉnh sửa sơ đồ:** draw.io Desktop hoặc draw.io trên trình duyệt.
- **Soạn thảo tài liệu:** Visual Studio Code hoặc trình soạn thảo Markdown tương đương.
- **Ngôn ngữ tài liệu:** Markdown.
- **Định dạng sơ đồ:** `.drawio`.

Không yêu cầu khởi chạy server hoặc kết nối cơ sở dữ liệu để đọc và kiểm tra các tài liệu phân tích.

## 3. Cấu trúc repository

```text
Chuyen-de-tot-nghiep1/
├── diagrams/
│   ├── business_flow_L2.drawio
│   └── use_case_L2.drawio
│
├── docs/
│   ├── ai-disclosure.md
│   ├── api-contract.md
│   ├── srs.md
│   └── usecase.drawio
│
├── .env.example
├── .gitignore
└── README.md
```

**Chức năng các thư mục:**

- `docs/`: Lưu tài liệu đặc tả, phân tích yêu cầu và sơ đồ Use Case.
- `diagrams/`: Lưu các sơ đồ mô tả luồng nghiệp vụ và Use Case.
- `.env.example`: Cung cấp mẫu các biến môi trường nếu cần cấu hình trong giai đoạn phát triển.
- `.gitignore`: Xác định các tệp và thư mục không đưa vào Git.
- `README.md`: Giới thiệu đề tài, cấu trúc repository và các tài liệu đã thực hiện.

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

## 6. Kết quả thực hiện Buổi 04

Các sản phẩm phân tích và đặc tả yêu cầu được xây dựng trong phạm vi bài thực hành gồm:

- Hoàn thành tài liệu SRS cho luồng L2.
- Xây dựng User Story và Acceptance Criteria theo phương pháp Given – When – Then.
- Xác định danh sách 9 Use Case và vai trò của các Actor.
- Đặc tả chi tiết UC05 – Tạo phiếu bảo hành.
- Xác định các yêu cầu chức năng (FR) và yêu cầu phi chức năng (NFR).
- Xây dựng bảng truy vết giữa User Story, Use Case và Functional Requirement.
- Xây dựng Use Case Diagram bằng draw.io.
- Xây dựng Business Flow cho quy trình tiếp nhận và phân loại yêu cầu bảo hành.
- Xây dựng API Contract đề xuất cho Track SE.
- Hoàn thiện tài liệu AI Disclosure.
- Hoàn thiện cấu trúc repository và các tệp cấu hình Git cơ bản.

Các tài liệu được tổ chức trong `docs/` và các sơ đồ được lưu trong `diagrams/` theo cấu trúc repository.

## 7. Phạm vi và giới hạn

Repository hiện tập trung vào phân tích nghiệp vụ, đặc tả yêu cầu và thiết kế ở mức tài liệu. Các API trong `docs/api-contract.md` là đề xuất phục vụ thiết kế, chưa khẳng định đã được triển khai hoặc kết nối với hệ thống thực tế của Mekong Mobile.

Việc triển khai giao diện, backend, cơ sở dữ liệu và kiểm thử tích hợp có thể được thực hiện ở giai đoạn tiếp theo nếu nằm trong phạm vi môn học.

## 8. Kết luận

Repository **Smart CRM – Mekong Mobile** là sản phẩm phân tích yêu cầu cho Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành. Các tài liệu được tổ chức nhằm thể hiện mối liên hệ giữa nghiệp vụ, User Story, Use Case, yêu cầu chức năng, yêu cầu phi chức năng và API Contract.

Đây là cơ sở để tiếp tục thiết kế hệ thống, xây dựng các thành phần phần mềm và kiểm thử yêu cầu trong những giai đoạn tiếp theo.