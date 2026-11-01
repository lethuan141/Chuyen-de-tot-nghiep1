# Smart CRM – Mekong Mobile
## 1. Giới thiệu đề tài
Đề tài tập trung phân tích và triển khai bước đầu Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành trong hệ thống Smart CRM của Mekong Mobile.

Mục tiêu là phân tích yêu cầu nghiệp vụ và chuyển đổi thành các tài liệu đặc tả phần mềm phục vụ thiết kế, phát triển và kiểm thử hệ thống, bao gồm SRS, User Story, Use Case, Business Flow và API Contract.

Phạm vi nghiệp vụ chính:

Tra cứu thông tin khách hàng.
Tạo hồ sơ khách hàng mới.
Ghi nhận thông tin thiết bị.
Kiểm tra tình trạng bảo hành.
Tạo phiếu bảo hành.
Ghi nhận mô tả lỗi.
Phân loại nhóm sự cố.
Xác định mức độ ưu tiên.
Sinh hạn cam kết xử lý.
## 2. Môi trường thực hiện
Dự án sử dụng Python, FastAPI và MySQL để xây dựng API phục vụ luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành.

### 2.1. Yêu cầu môi trường
Hệ điều hành: Windows 10/11.
Ngôn ngữ lập trình: Python 3.11.
Framework backend: FastAPI 0.115.6.
ASGI server: Uvicorn 0.34.0.
Cơ sở dữ liệu: MySQL Server 8.0 trở lên.
Thư viện kết nối MySQL: PyMySQL.
Quản lý biến môi trường: python-dotenv.
Quản lý mã nguồn: Git và GitHub.
Công cụ kiểm thử API: Swagger UI tại /docs.
Công cụ chỉnh sửa: Visual Studio Code hoặc trình soạn thảo tương đương.

### 2.2. Cài đặt và khởi chạy

Bước 1: Cài đặt thư viện backend

```bash
pip install fastapi==0.115.6 uvicorn==0.34.0 PyMySQL python-dotenv
```

Bước 2: Cấu hình môi trường

Tạo file `.env` tại thư mục gốc theo mẫu `.env.example` và cấu hình thông tin kết nối MySQL. Không đưa thông tin mật khẩu thật lên GitHub.

Bước 3: Khởi tạo cơ sở dữ liệu

Đảm bảo MySQL đang hoạt động, tạo cơ sở dữ liệu `smart_crm_mekong_mobile` và thực hiện các script SQL trong `migrations/` và `seed/`.

Bước 4: Khởi chạy backend

```bash
python -m uvicorn src.main:app --reload
```

Bước 5: Cài đặt thư viện frontend

Mở terminal mới tại thư mục dự án và chạy:

```bash
cd frontend
npm ci
```

Bước 6: Khởi chạy frontend

Tại thư mục `frontend`, chạy:

```bash
npm run dev
```

Bước 7: Kiểm tra frontend production build

Tại thư mục `frontend`, chạy:

```bash
npm run build
```

Bước 8: Chạy unit test backend

Tại thư mục gốc dự án, chạy:

```bash
python -m pytest -v
```

Địa chỉ truy cập

- Frontend: địa chỉ được Vite hiển thị trong terminal.
- Backend Swagger UI: `http://127.0.0.1:8000/docs`.

Lưu ý: Backend và frontend cần chạy trong hai cửa sổ terminal riêng.

## 3. Cấu trúc repository

```text
Chuyen-de-tot-nghiep1/
├── Diagram/
│   ├── business_flow_L2.drawio
│   ├── use_case_L2.drawio
│   ├── Database.drawio
│   ├── MÔ HÌNH.drawio
│   └── Wireframe1.drawio
├── docs/
│   ├── evidence/
│   ├── ai-disclosure.md
│   ├── api-contract.md
│   ├── api-test-results.md
│   ├── srs.md
│   ├── thay-doi-thiet-ke.md
│   └── usecase.drawio
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js
│   │   ├── components/
│   │   │   └── DataState.jsx
│   │   └── pages/
│   ├── package.json
│   └── package-lock.json
├── migrations/
│   └── 001_create_tables.sql
├── seed/
│   └── 001_seed_data.sql
├── src/
│   ├── routes/
│   ├── services/
│   ├── repositories/
│   ├── db.py
│   └── main.py
├── test_customer_device.py
├── test_sla.py
├── .env.example
├── .gitignore
└── README.md
```

**Chức năng chính:**

- `Diagram/`: Lưu trữ các sơ đồ phân tích và thiết kế hệ thống, bao gồm sơ đồ luồng nghiệp vụ, Use Case, cơ sở dữ liệu, mô hình hệ thống và Wireframe.
- `docs/`: Lưu trữ tài liệu đặc tả, hợp đồng API, kết quả kiểm thử, công khai sử dụng AI và nhật ký thay đổi thiết kế.
- `docs/evidence/`: Lưu ảnh minh chứng quá trình kiểm thử API và giao diện hệ thống.
- `frontend/src/pages/`: Chứa các màn hình danh sách, xem chi tiết và tiếp nhận phiếu bảo hành.
- `frontend/src/api/client.js`: Tập trung các hàm gọi API backend, hỗ trợ frontend trao đổi dữ liệu với hệ thống.
- `frontend/src/components/DataState.jsx`: Thành phần hiển thị các trạng thái tải dữ liệu, dữ liệu rỗng và lỗi.
- `migrations/`: Chứa các script SQL phục vụ khởi tạo cấu trúc cơ sở dữ liệu.
- `seed/`: Chứa các script SQL dùng để nạp dữ liệu mẫu.
- `src/routes/`: Tiếp nhận và định tuyến các yêu cầu HTTP đến những chức năng tương ứng.
- `src/services/`: Xử lý logic nghiệp vụ và kiểm tra dữ liệu đầu vào.
- `src/repositories/`: Thực hiện các thao tác truy vấn, thêm, sửa và xóa dữ liệu trong cơ sở dữ liệu.
- `src/db.py`: Thiết lập kết nối giữa ứng dụng backend và MySQL.
- `src/main.py`: Khởi tạo ứng dụng FastAPI và đăng ký các router.
- `test_customer_device.py`: Kiểm thử logic nghiệp vụ khách hàng và thiết bị, bao gồm các trường hợp dữ liệu hợp lệ, giá trị biên và dữ liệu không hợp lệ.
- `test_sla.py`: Kiểm thử các quy tắc tính thời hạn SLA, bao gồm giờ làm việc, thời gian nghỉ trưa, cuối tuần và các giá trị biên.
- `.env.example`: Cung cấp mẫu cấu hình các biến môi trường cần thiết để kết nối cơ sở dữ liệu.
- `.gitignore`: Quy định các tệp và thư mục không được đưa vào Git, chẳng hạn như tệp `.env` và các tệp phát sinh không cần thiết.
- `README.md`: Hướng dẫn cài đặt môi trường, cấu hình, khởi chạy hệ thống và thực hiện kiểm thử.
## 4. Danh sách tài liệu
Tài liệu	Nội dung
docs/srs.md	Đặc tả yêu cầu phần mềm, User Story, Acceptance Criteria, FR, NFR và Traceability.
docs/usecase.drawio	Sơ đồ Use Case được lưu trong thư mục tài liệu.
docs/api-contract.md	Mô tả hợp đồng API của dự án.
docs/api-test-results.md	Tổng hợp kết quả kiểm thử API.
docs/ai-disclosure.md	Công khai mục đích và phạm vi sử dụng công cụ AI trong quá trình thực hiện.
docs/thay-doi-thiet-ke.md	Nhật ký thay đổi thiết kế và trạng thái thực hiện Buổi 08.
Diagram/business_flow_L2.drawio	Sơ đồ luồng nghiệp vụ L2.
Diagram/use_case_L2.drawio	Sơ đồ Use Case tổng quan của luồng L2.
Diagram/Database.drawio	Sơ đồ cơ sở dữ liệu.
Diagram/MÔ HÌNH.drawio	Sơ đồ mô hình hệ thống.
Diagram/Wireframe1.drawio	Sơ đồ phác thảo giao diện.
Các tệp .drawio có thể được mở và chỉnh sửa bằng draw.io Desktop hoặc draw.io trên trình duyệt.

## 5. Luồng nghiệp vụ được phân tích
Mã luồng: L2

Tên luồng: Tiếp nhận và phân loại yêu cầu bảo hành.

### 5.1. Actor
Nhân viên tiếp nhận: Tiếp nhận thông tin khách hàng, thiết bị và yêu cầu bảo hành.
Quản lý trung tâm: Hỗ trợ xác minh tình trạng bảo hành trong các trường hợp cần kiểm tra thêm.
Hệ thống Smart CRM: Kiểm tra dữ liệu, lưu thông tin phiếu và xác định hạn cam kết theo quy tắc nghiệp vụ.
### 5.2. Danh sách Use Case
Mã	Tên Use Case
UC01	Tra cứu khách hàng
UC02	Tạo hồ sơ khách hàng
UC03	Ghi nhận thiết bị
UC04	Kiểm tra tình trạng bảo hành
UC05	Tạo phiếu bảo hành (Đặc tả)
UC06	Ghi nhận mô tả lỗi
UC07	Phân loại nhóm sự cố
UC08	Xác định mức ưu tiên
UC09	Sinh hạn cam kết
### 5.3. Mô tả khái quát quy trình
Nhân viên tiếp nhận tra cứu thông tin khách hàng bằng số điện thoại.
Nếu chưa có hồ sơ phù hợp, nhân viên tạo hồ sơ khách hàng mới.
Nhân viên tra cứu và ghi nhận thiết bị bằng Serial hoặc IMEI.
Hệ thống kiểm tra tình trạng bảo hành; trường hợp chưa đủ thông tin được chuyển xác minh theo quy trình.
Nhân viên ghi nhận mô tả lỗi của khách hàng.
Nhân viên phân loại nhóm sự cố và xác định mức ưu tiên.
Nhân viên tạo phiếu bảo hành với các thông tin bắt buộc hợp lệ.
Hệ thống sinh mã phiếu, xác định hạn cam kết theo quy tắc nghiệp vụ và lưu thông tin cần thiết.
## 6. Trạng thái tiến độ hiện tại
Dự án đã chuyển từ giai đoạn phân tích, đặc tả yêu cầu sang giai đoạn hiện thực và kiểm thử các API backend ban đầu cho luồng L2.

### 6.1. Cấu trúc mã nguồn
Đã tổ chức mã nguồn backend theo kiến trúc phân lớp:

src/routes/: Tiếp nhận và xử lý các yêu cầu HTTP.
src/services/: Xử lý logic nghiệp vụ.
src/repositories/: Truy vấn và ghi dữ liệu.
src/db.py: Thiết lập kết nối cơ sở dữ liệu.
src/main.py: Khởi tạo ứng dụng FastAPI và đăng ký router.
Đã chạy lệnh python -m compileall src để kiểm tra cú pháp mã nguồn.

### ### 6.2. Chức năng đã hiện thực và kiểm thử

Các chức năng backend đã triển khai bao gồm tra cứu và quản lý hồ sơ khách hàng, quản lý thông tin thiết bị, tạo và quản lý phiếu bảo hành. Mã nguồn được tổ chức theo kiến trúc phân lớp, trong đó Routes tiếp nhận yêu cầu HTTP, Services xử lý logic nghiệp vụ và Repositories thực hiện các thao tác với cơ sở dữ liệu.

**Kiểm thử API trên Swagger UI**

Các thao tác CRUD đối với khách hàng và thiết bị đã được kiểm thử trên Swagger UI, mỗi nhóm đạt 5/5 trường hợp kiểm thử thành công. Đối với phiếu bảo hành, các thao tác được kiểm thử như sau:

| Thao tác | API | Kết quả kiểm thử |
|---|---|---|
| Tạo phiếu | `POST /api/tickets` | Thành công – HTTP 201 |
| Xem danh sách | `GET /api/tickets` | Thành công – HTTP 200 |
| Xem chi tiết | `GET /api/tickets/{ticket_id}` | Thành công – HTTP 200 |
| Cập nhật phiếu | `PUT /api/tickets/{ticket_id}` | Thành công – HTTP 200 |
| Xóa phiếu kiểm thử | `DELETE /api/tickets/{ticket_id}` | Thành công – HTTP 200 |

**Kiểm thử các trường hợp ngoại lệ**

Bên cạnh các trường hợp xử lý thành công, hệ thống đã được kiểm tra một số tình huống dữ liệu không hợp lệ và lỗi nghiệp vụ:

- Truy cập phiếu bảo hành không tồn tại: hệ thống trả về HTTP 404.
- Thiếu trường bắt buộc khi tạo phiếu bảo hành: hệ thống trả về HTTP 422.
- Một số trường hợp dữ liệu khách hàng, thiết bị hoặc mức ưu tiên không hợp lệ đã được kiểm tra thông qua các API tương ứng.
- Các ảnh minh chứng kiểm thử API được lưu trong thư mục `docs/evidence/`.

**Kiểm thử tự động bằng pytest**

Dự án đã xây dựng bộ kiểm thử tự động gồm 14 trường hợp kiểm thử, được tổ chức trong hai tệp:

- `test_customer_device.py`: gồm 8 trường hợp kiểm thử logic nghiệp vụ khách hàng và thiết bị, bao gồm dữ liệu hợp lệ (Happy Path), giá trị biên (Boundary Value) và dữ liệu không hợp lệ (Invalid Data).
- `test_sla.py`: gồm 6 trường hợp kiểm thử quy tắc tính thời hạn SLA, bao gồm giờ làm việc, thời gian nghỉ trưa, cuối tuần và các giá trị biên.

Bộ kiểm thử được thực thi bằng lệnh:

```bash
python -m pytest -v
```

Kết quả thực tế: **14/14 test passed**, không có trường hợp kiểm thử nào thất bại.

Kết quả kiểm thử API được tổng hợp trong `docs/api-test-results.md`; các ảnh minh chứng tương ứng được lưu tại `docs/evidence/`. Bộ unit test hỗ trợ kiểm tra logic nghiệp vụ và các quy tắc xử lý dữ liệu. Đây là kết quả kiểm thử tự động ở mức unit test, không thay thế cho kiểm thử tích hợp toàn bộ hệ thống.

### 6.3. Cơ sở dữ liệu
Repository có các script dự kiến phục vụ khởi tạo cấu trúc và dữ liệu mẫu:

migrations/001_create_tables.sql: Script tạo các bảng nghiệp vụ.
seed/001_seed_data.sql: Script nạp dữ liệu mẫu.
Cần tiếp tục rà soát cấu trúc bảng, khóa ngoại, ràng buộc dữ liệu và tính nhất quán giữa migration, seed với thiết kế cơ sở dữ liệu đã thống nhất trong BT1 trước khi xác nhận hoàn thành hạng mục này.

### 6.4. Tài liệu, bảo mật và minh chứng
Đã có tài liệu SRS, API Contract, Use Case và AI Disclosure.
Đã cập nhật docs/thay-doi-thiet-ke.md để ghi nhận các quyết định thiết kế và tiến độ Buổi 08.
Đã có docs/api-test-results.md để tổng hợp các trường hợp kiểm thử API.
Đã có thư mục docs/evidence/ chứa ảnh minh chứng cho các API đã kiểm thử.
Đã kiểm tra .gitignore để bỏ qua file .env và các tệp không nên đưa vào Git.
Đã kiểm tra .env.example; thông tin mật khẩu trong tệp mẫu sử dụng giá trị giữ chỗ.
Cần bổ sung ảnh minh chứng cho các thao tác CRUD còn thiếu nếu chưa được lưu đầy đủ.
### 6.5. Git và phiên bản mã nguồn

Các thay đổi của dự án đã được quản lý bằng Git và đẩy lên nhánh `main` của GitHub.

Một số commit tiêu biểu:

- `afc1d29` – `feat: complete warranty ticket CRUD API`
- `82ea8d3` – `docs: update design change log for lab 08`
- `ce83a3e` – `test: complete warranty ticket E2E evidence`

Commit mới nhất được ghi nhận trong quá trình thực hiện Buổi 10 là `ce83a3e`.

Repository: https://github.com/lethuan141/Chuyen-de-tot-nghiep1

Trạng thái đồng bộ và tính sạch của working tree cần được xác nhận bằng kết quả Git tại thời điểm kiểm tra.


### ### 6.6. Tiến độ Buổi 10

**Frontend**

- Đã xây dựng giao diện frontend bằng React/Vite cho màn hình danh sách phiếu bảo hành.
- Đã xây dựng giao diện xem thông tin chi tiết phiếu bảo hành.
- Đã xây dựng giao diện tiếp nhận yêu cầu và tạo phiếu bảo hành.
- Đã tổ chức các hàm gọi API backend tập trung tại `frontend/src/api/client.js`, hỗ trợ các màn hình frontend trao đổi dữ liệu với hệ thống.
- Đã sử dụng component `DataState` để xử lý các trạng thái tải dữ liệu (Loading), không có dữ liệu (Empty) và lỗi (Error) trên màn hình danh sách và chi tiết.
- Đã điều chỉnh các giá trị mức độ ưu tiên trên biểu mẫu tạo phiếu để thống nhất với các giá trị mà backend đang sử dụng.
- Đã thực hiện kiểm tra frontend production build bằng lệnh `npm run build`; kết quả build thành công.

**Kiểm thử**

- Đã xây dựng bộ kiểm thử tự động gồm 14 unit test, trong đó có 8 trường hợp kiểm thử logic nghiệp vụ khách hàng và thiết bị trong `test_customer_device.py`, cùng 6 trường hợp kiểm thử quy tắc tính thời hạn SLA trong `test_sla.py`.
- Các trường hợp kiểm thử khách hàng và thiết bị bao gồm luồng xử lý hợp lệ (Happy Path), kiểm tra giá trị biên (Boundary Value) và dữ liệu không hợp lệ (Invalid Data).
- Bộ kiểm thử SLA tập trung vào các quy tắc tính thời gian xử lý, bao gồm giờ làm việc, thời gian nghỉ trưa, cuối tuần và các giá trị biên.
- Đã chạy bộ kiểm thử bằng lệnh `python -m pytest -v`; kết quả: **14/14 test passed**.
- Đã kiểm tra cú pháp mã nguồn backend bằng lệnh `python -m compileall src`.
- Đã lưu ảnh minh chứng giao diện tạo phiếu, danh sách phiếu và chi tiết phiếu trong thư mục `docs/evidence/`.
- Đã thực hiện kiểm thử các API backend trên Swagger UI, bao gồm các thao tác CRUD và một số trường hợp dữ liệu không hợp lệ. Kết quả được tổng hợp trong `docs/api-test-results.md`.
- Kiểm thử End-to-End (E2E) cần được xác nhận dựa trên kết quả thực chạy toàn bộ luồng nghiệp vụ từ giao diện: tiếp nhận thông tin, tạo phiếu bảo hành, xem chi tiết và kiểm tra phiếu trong danh sách. Không sử dụng kết quả production build hoặc unit test để thay thế bằng chứng kiểm thử E2E.
- Kết quả kiểm tra lint cần được ghi nhận theo lần chạy thực tế, bao gồm trạng thái thành công hoặc các cảnh báo, lỗi còn tồn tại.

**Tài liệu và quản lý mã nguồn**

- Đã cập nhật `README.md` với hướng dẫn cài đặt môi trường, cấu hình cơ sở dữ liệu, khởi chạy backend, frontend và thực hiện kiểm thử tự động.
- Đã cập nhật nội dung tài liệu nhằm phản ánh cấu trúc mã nguồn, các chức năng đã triển khai và kết quả kiểm thử thực tế.
- Đã tổ chức các tài liệu và ảnh minh chứng kiểm thử trong thư mục `docs/` và `docs/evidence/`.
- Đã sử dụng Git để quản lý phiên bản mã nguồn và GitHub để lưu trữ repository.
- Commit mới nhất được ghi nhận trong quá trình thực hiện Buổi 10 là `ce83a3e` (`test: complete warranty ticket E2E evidence`), trên nhánh `main`. Trạng thái commit và đồng bộ repository cần được xác nhận lại bằng các lệnh Git tại thời điểm kiểm tra.
- Việc thiết lập dự án từ một bản clone sạch cần được kiểm tra bằng cách clone repository, cài đặt các thư viện cần thiết, cấu hình môi trường và khởi chạy thử hệ thống.

**Đánh giá tiến độ**

Sau Buổi 10, dự án đã có các màn hình frontend cơ bản phục vụ nghiệp vụ tiếp nhận và quản lý phiếu bảo hành, các API backend tương ứng, cùng bộ kiểm thử tự động 14 trường hợp đạt kết quả thành công. Frontend production build cũng đã được kiểm tra thành công.

Các hạng mục cần tiếp tục xác minh và hoàn thiện gồm kiểm thử E2E trên giao diện, kết quả lint, khả năng thiết lập dự án từ bản clone sạch và tính đồng bộ giữa tài liệu, mã nguồn và ảnh minh chứng. Chỉ xác nhận hoàn thành các hạng mục này khi đã thực hiện kiểm tra và có kết quả thực tế.
## 7. Phạm vi và giới hạn
Repository tập trung vào phân tích nghiệp vụ, đặc tả yêu cầu và triển khai bước đầu các API backend cho Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành.

Các API được mô tả trong docs/api-contract.md cần được đối chiếu với mã nguồn thực tế; không mặc định rằng mọi API trong tài liệu đều đã được triển khai. Dự án cũng chưa được khẳng định là đã hoàn thành kiểm thử tích hợp hoặc triển khai trên môi trường vận hành thực tế của Mekong Mobile.
## ## 8. Kết luận

Repository Smart CRM – Mekong Mobile tập trung vào phân tích yêu cầu và triển khai bước đầu Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành.

Dự án đã xây dựng các tài liệu đặc tả nghiệp vụ, triển khai các chức năng backend cho khách hàng, thiết bị và phiếu bảo hành, đồng thời phát triển giao diện frontend phục vụ danh sách, xem chi tiết và tạo phiếu.

Bộ kiểm thử tự động hiện có 14 unit test, bao gồm kiểm thử nghiệp vụ khách hàng, thiết bị và quy tắc SLA. Kết quả chạy pytest đạt 14/14 test passed. Frontend cũng đã được kiểm tra production build thành công.

Các kết quả này tạo cơ sở để tiếp tục hoàn thiện tính nhất quán giữa tài liệu và mã nguồn, kiểm thử tích hợp, rà soát cơ sở dữ liệu và nâng cao độ ổn định của hệ thống. Phạm vi hoàn thành cần được xác nhận dựa trên kết quả thực tế của từng hạng mục.