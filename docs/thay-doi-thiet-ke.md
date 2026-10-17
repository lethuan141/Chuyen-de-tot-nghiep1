\# NHẬT KÝ THAY ĐỔI THIẾT KẾ – BUỔI 08



\## 1. Thông tin chung



\- \*\*Dự án:\*\* Smart CRM – Mekong Mobile

\- \*\*Luồng nghiệp vụ:\*\* L2 – Tiếp nhận và phân loại yêu cầu bảo hành

\- \*\*Track:\*\* SE

\- \*\*Kiến trúc:\*\* Layered Architecture

\- \*\*Công nghệ:\*\* Python, FastAPI, MySQL

\- \*\*Repository:\*\* https://github.com/lethuan141/Chuyen-de-tot-nghiep1



\## 2. Phản hồi BT1 từ giảng viên



\- \*\*Phản hồi của giảng viên:\*\* Chưa cập nhật nội dung phản hồi thực tế.

\- \*\*Trạng thái tiếp nhận:\*\* Cần bổ sung sau khi nhận hoặc rà soát phản hồi của giảng viên.

\- \*\*Hướng xử lý:\*\* Đối chiếu thiết kế và tài liệu BT1 với cấu trúc mã nguồn, cơ sở dữ liệu và các chức năng backend đã triển khai để phát hiện những điểm cần điều chỉnh.



\## 3. Quyết định thiết kế



\- Giữ nguyên kiến trúc phân lớp gồm `routes`, `services` và `repositories` để tách biệt xử lý HTTP, nghiệp vụ và truy cập cơ sở dữ liệu.

\- Tiếp tục sử dụng Python, FastAPI và MySQL theo định hướng công nghệ của dự án.

\- Sử dụng thư mục `migrations/` để quản lý các tập lệnh khởi tạo hoặc thay đổi cấu trúc cơ sở dữ liệu.

\- Sử dụng thư mục `seed/` để lưu dữ liệu mẫu phục vụ quá trình kiểm thử.

\- Bổ sung các thao tác CRUD cho thực thể chính là phiếu bảo hành, bao gồm tạo mới, truy vấn danh sách, truy vấn chi tiết, cập nhật và xóa.

\- Kiểm tra sự tồn tại của phiếu bảo hành trước khi thực hiện thao tác cập nhật hoặc xóa để xử lý trường hợp mã phiếu không tồn tại.

\- Bổ sung quy tắc ngăn xóa phiếu bảo hành đã có lịch sử trạng thái nhằm hạn chế ảnh hưởng đến dữ liệu nghiệp vụ.

\- Sử dụng các mã trạng thái HTTP phù hợp để phản hồi kết quả xử lý API.



\## 4. Các điểm cần kiểm chứng



\- Đối chiếu cấu trúc bảng trong migration với mô hình dữ liệu đã xác định trong BT1.

\- Kiểm tra tính nhất quán giữa migration, dữ liệu seed và cấu trúc cơ sở dữ liệu thực tế.

\- Rà soát quy tắc tính hạn cam kết SLA theo mức ưu tiên và lịch làm việc.

\- Kiểm tra quy tắc ngăn tạo phiếu bảo hành đang xử lý trùng thiết bị.

\- Kiểm tra khả năng tra cứu khách hàng bằng số điện thoại và thiết bị bằng Serial/IMEI.

\- Bổ sung ảnh minh chứng cho các thao tác CRUD phiếu bảo hành trên Swagger UI.

\- Đối chiếu kết quả kiểm thử với nội dung trong `docs/api-test-results.md` để bảo đảm tài liệu phản ánh đúng kết quả thực tế.



\## 5. Lý do kỹ thuật



Kiến trúc phân lớp giúp mã nguồn dễ kiểm thử, bảo trì và mở rộng. Lớp `routes` tiếp nhận yêu cầu HTTP và trả về phản hồi cho phía gọi API; lớp `services` xử lý các quy tắc nghiệp vụ; lớp `repositories` đảm nhiệm việc truy vấn và thay đổi dữ liệu trong cơ sở dữ liệu.



Việc sử dụng migration giúp quản lý các thay đổi về cấu trúc cơ sở dữ liệu có hệ thống. Dữ liệu seed hỗ trợ kiểm thử với dữ liệu mẫu. Bên cạnh đó, việc kiểm tra sự tồn tại của phiếu bảo hành trước khi cập nhật hoặc xóa giúp hạn chế thao tác trên dữ liệu không hợp lệ. Quy tắc bảo vệ phiếu đã có lịch sử trạng thái cũng góp phần duy trì tính toàn vẹn của dữ liệu nghiệp vụ.



\## 6. Trạng thái thực hiện



\### 6.1. Cấu trúc mã nguồn



\- Đã tổ chức mã nguồn backend theo ba lớp `src/routes/`, `src/services/` và `src/repositories/`.

\- Đã bổ sung xử lý API CRUD phiếu bảo hành trong các lớp tương ứng.

\- Đã chạy lệnh `python -m compileall src` và không phát hiện lỗi cú pháp ở các tệp được kiểm tra.



\### 6.2. CRUD phiếu bảo hành



Các thao tác CRUD đã được triển khai và kiểm thử trên Swagger UI:



\- \*\*Create:\*\* Tạo phiếu bảo hành mới bằng `POST /api/tickets`, kiểm thử thành công với HTTP 201.

\- \*\*Read:\*\* Truy vấn danh sách bằng `GET /api/tickets` và chi tiết bằng `GET /api/tickets/{ticket\_id}`, kiểm thử thành công với HTTP 200.

\- \*\*Update:\*\* Cập nhật thông tin phiếu bằng `PUT /api/tickets/{ticket\_id}`, kiểm thử thành công với HTTP 200.

\- \*\*Delete:\*\* Xóa phiếu kiểm thử bằng `DELETE /api/tickets/{ticket\_id}`, kiểm thử thành công với HTTP 200.

\- \*\*Xử lý ngoại lệ:\*\* Đã kiểm thử trường hợp truy cập phiếu không tồn tại và nhận HTTP 404.



Các trường hợp kiểm thử dữ liệu không hợp lệ khác được tổng hợp trong `docs/api-test-results.md` và cần tiếp tục đối chiếu với kết quả thực tế.



\### 6.3. Migration và dữ liệu seed



\- Dự án có thư mục `migrations/` để lưu các tập lệnh tạo hoặc thay đổi cấu trúc cơ sở dữ liệu.

\- Dự án có thư mục `seed/` để lưu tập lệnh dữ liệu mẫu.

\- Cần tiếp tục đối chiếu migration và seed với mô hình dữ liệu BT1 để xác nhận tính nhất quán trước khi đánh dấu hoàn thành hạng mục này.



\### 6.4. Tài liệu và ảnh minh chứng



\- Đã có tài liệu API Contract tại `docs/api-contract.md`.

\- Đã có tài liệu tổng hợp kết quả kiểm thử tại `docs/api-test-results.md`.

\- Đã có tài liệu SRS tại `docs/srs.md` và AI Disclosure tại `docs/ai-disclosure.md`.

\- Thư mục `docs/evidence/` hiện có ảnh minh chứng cho các API khách hàng, thiết bị và tạo phiếu bảo hành.

\- Cần bổ sung ảnh minh chứng cho thao tác truy vấn danh sách phiếu, xem chi tiết, cập nhật và xóa phiếu bảo hành.



\### 6.5. Git và phiên bản mã nguồn



\- Đã kiểm tra `.gitignore` để bỏ qua tệp môi trường `.env`, môi trường ảo, thư viện và dữ liệu lớn.

\- Đã kiểm tra `.env.example`; mật khẩu cơ sở dữ liệu trong tệp mẫu đang sử dụng giá trị giữ chỗ.

\- Đã xác nhận `.env` được Git bỏ qua và không nằm trong danh sách tệp đang được theo dõi.

\- Đã tạo commit `afc1d29` với nội dung `feat: complete warranty ticket CRUD API`.

\- Đã push commit lên nhánh `main` của repository GitHub.

\- Commit: https://github.com/lethuan141/Chuyen-de-tot-nghiep1/commit/afc1d29



\### 6.6. Công việc tiếp theo



\- Bổ sung ảnh minh chứng còn thiếu cho các thao tác CRUD phiếu bảo hành.

\- Rà soát và cập nhật README để phản ánh đúng trạng thái triển khai backend.

\- Kiểm tra tính nhất quán giữa migration, seed và thiết kế dữ liệu BT1.

\- Hoàn thiện tài liệu kiểm thử, nhật ký thay đổi thiết kế và các minh chứng theo yêu cầu Buổi 08.

\- Tiếp tục kiểm thử các trường hợp ngoại lệ và xác nhận kết quả trước khi chốt báo cáo.

