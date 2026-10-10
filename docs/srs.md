# SRS RÚT GỌN – SMART CRM MEKONG MOBILE

**Họ tên:** Lê Văn Thuận  
**MSSV:** 2374802010487  
**Track:** SE  
**Luồng nghiệp vụ:** L2 – Tiếp nhận và phân loại yêu cầu bảo hành

## 1. Tổng quan

### 1.1. Phạm vi

Tài liệu mô tả các yêu cầu phần mềm thuộc Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành của hệ thống Smart CRM Mekong Mobile.

Hệ thống hỗ trợ nhân viên tiếp nhận tra cứu khách hàng, tạo hồ sơ khách hàng mới, ghi nhận thiết bị, kiểm tra tình trạng bảo hành, tạo phiếu bảo hành, nhập mô tả lỗi, phân loại nhóm sự cố, xác định mức ưu tiên và sinh hạn cam kết xử lý.

Tài liệu tập trung vào việc xác định yêu cầu chức năng, yêu cầu phi chức năng, User Story, Use Case, tiêu chí chấp nhận và mối quan hệ truy vết giữa các yêu cầu.

### 1.2. Người dùng chính

- **Nhân viên tiếp nhận:** Trực tiếp tiếp nhận yêu cầu bảo hành, tra cứu khách hàng, ghi nhận thông tin thiết bị và tạo phiếu bảo hành.
- **Quản lý trung tâm:** Hỗ trợ xác minh các trường hợp bảo hành chưa đủ thông tin hoặc cần kiểm tra thêm.
- **Hệ thống Smart CRM:** Kiểm tra dữ liệu, lưu thông tin, sinh mã phiếu, xác định hạn cam kết và ghi nhận lịch sử thay đổi.

### 1.3. Các thực thể liên quan

| Thực thể | Mô tả |
|---|---|
| `customer` | Lưu thông tin khách hàng. |
| `device` | Lưu thông tin thiết bị và mã định danh. |
| `ticket` | Lưu thông tin phiếu bảo hành. |
| `issue_category` | Lưu danh mục nhóm sự cố. |
| `ticket_status_log` | Lưu lịch sử thay đổi trạng thái phiếu bảo hành. |

### 1.4. Bảng thuật ngữ

| Thuật ngữ | Giải thích |
|---|---|
| CRM | Customer Relationship Management – hệ thống quản lý quan hệ khách hàng. |
| Ticket | Phiếu yêu cầu bảo hành. |
| Serial/IMEI | Mã định danh thiết bị. |
| Issue Category | Nhóm sự cố dùng để phân loại yêu cầu bảo hành. |
| Priority | Mức độ ưu tiên xử lý yêu cầu. |
| SLA | Thời hạn cam kết xử lý yêu cầu. |
| GWT | Given – When – Then, phương pháp mô tả tiêu chí chấp nhận. |
| MoSCoW | Phương pháp phân loại mức độ ưu tiên yêu cầu. |
| SRS | Software Requirements Specification – tài liệu đặc tả yêu cầu phần mềm. |
| API | Application Programming Interface – giao diện lập trình ứng dụng. |

## 2. User Story và tiêu chí chấp nhận

### US01 – Tra cứu khách hàng

**Mức ưu tiên:** MUST

**User Story:**

Là nhân viên tiếp nhận, em muốn tra cứu khách hàng bằng số điện thoại để xác định đúng hồ sơ khách hàng trước khi tiếp nhận yêu cầu bảo hành.

**Tiêu chí chấp nhận:**

- **GWT01:** Given số điện thoại hợp lệ, When nhân viên thực hiện tra cứu, Then hệ thống hiển thị hồ sơ khách hàng tương ứng.
- **GWT02:** Given số điện thoại chưa tồn tại, When nhân viên thực hiện tra cứu, Then hệ thống thông báo không tìm thấy hồ sơ và cho phép tạo hồ sơ mới.
- **GWT03 – Ngoại lệ:** Given số điện thoại đã tồn tại, When nhân viên tra cứu hoặc tạo lại hồ sơ, Then hệ thống sử dụng hồ sơ hiện có và không tạo bản ghi trùng.

### US02 – Tạo hồ sơ khách hàng

**Mức ưu tiên:** MUST

**User Story:**

Là nhân viên tiếp nhận, em muốn tạo hồ sơ khách hàng mới khi chưa tìm thấy thông tin để có dữ liệu phục vụ quá trình tiếp nhận bảo hành.

**Tiêu chí chấp nhận:**

- **GWT04:** Given số điện thoại chưa tồn tại, When nhân viên nhập đầy đủ thông tin hợp lệ, Then hệ thống tạo hồ sơ khách hàng mới.
- **GWT05:** Given số điện thoại được nhập theo định dạng được hỗ trợ, When hệ thống lưu hồ sơ, Then hệ thống chuẩn hóa số điện thoại theo quy định.
- **GWT06 – Ngoại lệ:** Given số điện thoại đã tồn tại, When nhân viên cố tạo hồ sơ mới, Then hệ thống từ chối tạo bản ghi trùng và thông báo phù hợp.

### US03 – Ghi nhận thiết bị

**Mức ưu tiên:** MUST

**User Story:**

Là nhân viên tiếp nhận, em muốn tra cứu và ghi nhận thiết bị bằng serial hoặc IMEI để xác định chính xác thiết bị của khách hàng.

**Tiêu chí chấp nhận:**

- **GWT07:** Given serial hoặc IMEI hợp lệ, When nhân viên thực hiện tra cứu, Then hệ thống hiển thị thông tin thiết bị tương ứng.
- **GWT08:** Given thiết bị thuộc khách hàng đang được tra cứu, When nhân viên ghi nhận thiết bị, Then hệ thống liên kết thiết bị với đúng khách hàng.
- **GWT09 – Ngoại lệ:** Given thiết bị đã được liên kết với khách hàng khác, When nhân viên thực hiện liên kết, Then hệ thống từ chối liên kết không hợp lệ và yêu cầu xác minh.

### US04 – Kiểm tra tình trạng bảo hành

**Mức ưu tiên:** MUST

**User Story:**

Là nhân viên tiếp nhận, em muốn kiểm tra tình trạng bảo hành của thiết bị để xác định điều kiện tiếp nhận yêu cầu.

**Tiêu chí chấp nhận:**

- **GWT10:** Given thiết bị có đầy đủ thông tin ngày mua và thời hạn bảo hành, When hệ thống kiểm tra, Then hệ thống xác định tình trạng bảo hành theo quy tắc nghiệp vụ.
- **GWT11:** Given thiết bị thiếu thông tin cần thiết, When nhân viên kiểm tra, Then hệ thống đánh dấu tình trạng bảo hành chưa được xác minh.
- **GWT12 – Ngoại lệ:** Given tình trạng bảo hành chưa được xác minh, When yêu cầu cần được tiếp tục xử lý, Then hệ thống hỗ trợ chuyển trường hợp đến quản lý trung tâm để xác minh.

### US05 – Tạo phiếu bảo hành

**Mức ưu tiên:** MUST

**User Story:**

Là nhân viên tiếp nhận, em muốn tạo phiếu bảo hành từ thông tin khách hàng, thiết bị và yêu cầu đã ghi nhận để lưu trữ và theo dõi quá trình xử lý.

**Tiêu chí chấp nhận:**

- **GWT13:** Given khách hàng và thiết bị đã được xác định, When nhân viên tạo phiếu với đầy đủ thông tin bắt buộc, Then hệ thống tạo phiếu bảo hành mới.
- **GWT14:** Given phiếu bảo hành được tạo thành công, When hệ thống trả kết quả, Then phiếu có mã định danh duy nhất và trạng thái ban đầu theo quy định.
- **GWT15 – Ngoại lệ:** Given thông tin khách hàng, thiết bị hoặc dữ liệu bắt buộc không hợp lệ, When nhân viên tạo phiếu, Then hệ thống từ chối tạo phiếu và thông báo lỗi tương ứng.

### US06 – Ghi nhận mô tả lỗi

**Mức ưu tiên:** MUST

**User Story:**

Là nhân viên tiếp nhận, em muốn ghi nhận mô tả lỗi do khách hàng cung cấp để lưu lại nội dung yêu cầu bảo hành.

**Tiêu chí chấp nhận:**

- **GWT16:** Given khách hàng cung cấp thông tin lỗi, When nhân viên nhập mô tả, Then hệ thống lưu nội dung vào phiếu bảo hành.
- **GWT17:** Given mô tả lỗi đã được lưu, When nhân viên xem lại phiếu, Then hệ thống hiển thị đầy đủ nội dung đã nhập.
- **GWT18 – Ngoại lệ:** Given mô tả lỗi chưa được nhập, When nhân viên hoàn tất bước tiếp nhận, Then hệ thống yêu cầu bổ sung thông tin bắt buộc.

### US07 – Phân loại nhóm sự cố

**Mức ưu tiên:** MUST

**User Story:**

Là nhân viên tiếp nhận, em muốn phân loại yêu cầu theo nhóm sự cố phù hợp để chuẩn hóa thông tin và hỗ trợ quá trình xử lý bảo hành.

**Tiêu chí chấp nhận:**

- **GWT19:** Given mô tả lỗi đã được ghi nhận, When nhân viên chọn nhóm sự cố, Then hệ thống lưu nhóm sự cố cho phiếu.
- **GWT20:** Given nhóm sự cố thuộc danh mục hợp lệ, When nhân viên xác nhận, Then hệ thống ghi nhận nhóm sự cố tương ứng.
- **GWT21 – Ngoại lệ:** Given nhân viên chưa chọn nhóm sự cố, When nhân viên hoàn tất bước phân loại, Then hệ thống yêu cầu chọn nhóm sự cố.

### US08 – Xác định mức ưu tiên

**Mức ưu tiên:** SHOULD

**User Story:**

Là nhân viên tiếp nhận, em muốn xác định mức ưu tiên cho phiếu bảo hành để làm căn cứ xác định thời hạn xử lý.

**Tiêu chí chấp nhận:**

- **GWT22:** Given phiếu đã được tiếp nhận, When nhân viên chọn mức ưu tiên, Then hệ thống lưu một trong các mức ưu tiên hợp lệ.
- **GWT23:** Given mức ưu tiên đã được xác định, When hệ thống tính hạn cam kết, Then thời hạn được xác định theo quy tắc tương ứng.
- **GWT24 – Ngoại lệ:** Given mức ưu tiên không hợp lệ, When nhân viên xác nhận, Then hệ thống thông báo lỗi và không lưu giá trị không hợp lệ.

### US09 – Sinh hạn cam kết

**Mức ưu tiên:** MUST

**User Story:**

Là nhân viên tiếp nhận, em muốn hệ thống tự động sinh hạn cam kết theo mức ưu tiên để giảm thao tác tính toán thủ công và hỗ trợ theo dõi thời hạn xử lý.

**Tiêu chí chấp nhận:**

- **GWT25:** Given mức ưu tiên là `CAO`, When hệ thống tính hạn cam kết, Then hệ thống áp dụng thời hạn tương ứng với mức ưu tiên cao.
- **GWT26:** Given mức ưu tiên là `TRUNG_BINH`, When hệ thống tính hạn cam kết, Then hệ thống áp dụng thời hạn tương ứng với mức ưu tiên trung bình.
- **GWT27:** Given mức ưu tiên là `THAP`, When hệ thống tính hạn cam kết, Then hệ thống áp dụng thời hạn tương ứng với mức ưu tiên thấp.
- **GWT28 – Ngoại lệ:** Given hệ thống xác định hạn cam kết, When tính thời hạn xử lý, Then hệ thống áp dụng quy tắc ngày làm việc và lịch nghỉ đã được cấu hình.

*Lưu ý: Thời hạn cụ thể của từng mức ưu tiên cần được xác nhận theo quy định nghiệp vụ trước khi triển khai.*

## 3. Use Case

### 3.1. Danh sách Use Case

| Mã | Tên Use Case | Actor chính | Mức ưu tiên |
|---|---|---|---|
| UC01 | Tra cứu khách hàng | Nhân viên tiếp nhận | MUST |
| UC02 | Tạo hồ sơ khách hàng | Nhân viên tiếp nhận | MUST |
| UC03 | Ghi nhận thiết bị | Nhân viên tiếp nhận | MUST |
| UC04 | Kiểm tra tình trạng bảo hành | Nhân viên tiếp nhận, Quản lý trung tâm | MUST |
| UC05 | Tạo phiếu bảo hành (Đặc tả) | Nhân viên tiếp nhận | MUST |
| UC06 | Ghi nhận mô tả lỗi | Nhân viên tiếp nhận | MUST |
| UC07 | Phân loại nhóm sự cố | Nhân viên tiếp nhận | MUST |
| UC08 | Xác định mức ưu tiên | Nhân viên tiếp nhận | SHOULD |
| UC09 | Sinh hạn cam kết | Hệ thống Smart CRM | MUST |

### 3.2. Mô tả trách nhiệm của Actor

| Actor | Trách nhiệm |
|---|---|
| Nhân viên tiếp nhận | Tra cứu khách hàng, tạo hồ sơ, ghi nhận thiết bị, kiểm tra bảo hành, tạo phiếu, nhập mô tả lỗi, phân loại sự cố và xác định mức ưu tiên. |
| Quản lý trung tâm | Xác minh các trường hợp bảo hành chưa đủ thông tin hoặc cần kiểm tra thêm. |
| Hệ thống Smart CRM | Kiểm tra dữ liệu, lưu thông tin, sinh mã phiếu, xác định hạn cam kết và ghi nhận lịch sử thay đổi. |

### 3.3. Đặc tả Use Case UC05 – Tạo phiếu bảo hành

**Mã Use Case:** UC05

**Tên Use Case:** Tạo phiếu bảo hành

**Actor chính:** Nhân viên tiếp nhận

**Mục tiêu:** Tạo phiếu bảo hành cho khách hàng sau khi đã xác định thông tin khách hàng, thiết bị và nội dung yêu cầu.

**Điều kiện tiên quyết:**

- Nhân viên tiếp nhận đã truy cập hệ thống.
- Khách hàng đã được xác định hoặc đã có hồ sơ hợp lệ.
- Thiết bị đã được xác định.
- Thông tin bảo hành đã được kiểm tra hoặc được đánh dấu chờ xác minh theo quy trình nghiệp vụ.

**Luồng chính:**

1. Nhân viên tiếp nhận chọn chức năng tạo phiếu bảo hành.
2. Hệ thống hiển thị biểu mẫu tạo phiếu.
3. Nhân viên chọn khách hàng và thiết bị.
4. Nhân viên nhập mô tả lỗi.
5. Nhân viên chọn nhóm sự cố.
6. Nhân viên xác định mức ưu tiên theo quy định.
7. Hệ thống kiểm tra tính hợp lệ của dữ liệu.
8. Hệ thống sinh mã phiếu bảo hành duy nhất.
9. Hệ thống xác định hạn cam kết theo quy tắc nghiệp vụ.
10. Hệ thống lưu phiếu và thông tin liên quan.
11. Hệ thống thông báo tạo phiếu thành công.

**Luồng ngoại lệ:**

- **E1 – Thiếu thông tin:** Nếu thiếu dữ liệu bắt buộc, hệ thống thông báo các trường cần bổ sung và không tạo phiếu.
- **E2 – Dữ liệu không hợp lệ:** Nếu khách hàng, thiết bị hoặc nhóm sự cố không hợp lệ, hệ thống thông báo lỗi và yêu cầu kiểm tra lại.
- **E3 – Chưa xác minh bảo hành:** Nếu thông tin bảo hành chưa đầy đủ, hệ thống ghi nhận trạng thái chờ xác minh hoặc chuyển quản lý trung tâm theo quy trình được cấu hình.

**Điều kiện hậu tiên quyết:**

- Phiếu bảo hành được lưu thành công với mã phiếu duy nhất.
- Thông tin khách hàng, thiết bị, mô tả lỗi, nhóm sự cố và mức ưu tiên được ghi nhận theo dữ liệu hợp lệ.
- Hạn cam kết được xác định khi đủ điều kiện áp dụng quy tắc SLA.
- Lịch sử tạo phiếu được ghi nhận theo quy định hệ thống.

## 4. Yêu cầu chức năng

| Mã | Mô tả yêu cầu |
|---|---|
| FR01 | Hệ thống cho phép tra cứu khách hàng bằng số điện thoại. |
| FR02 | Hệ thống cho phép tạo hồ sơ khách hàng mới khi chưa tìm thấy thông tin phù hợp. |
| FR03 | Hệ thống cho phép tra cứu và ghi nhận thiết bị bằng serial hoặc IMEI. |
| FR04 | Hệ thống cho phép kiểm tra và ghi nhận tình trạng bảo hành của thiết bị. |
| FR05 | Hệ thống cho phép tạo phiếu bảo hành khi thông tin khách hàng, thiết bị và các dữ liệu bắt buộc hợp lệ. |
| FR06 | Hệ thống cho phép ghi nhận và xem lại mô tả lỗi của khách hàng. |
| FR07 | Hệ thống cho phép phân loại yêu cầu bảo hành theo danh mục nhóm sự cố. |
| FR08 | Hệ thống cho phép xác định mức ưu tiên cho phiếu bảo hành. |
| FR09 | Hệ thống tự động xác định hạn cam kết dựa trên mức ưu tiên và quy tắc ngày làm việc. |

## 5. Yêu cầu phi chức năng

| Mã | Yêu cầu | Tiêu chí đánh giá |
|---|---|---|
| NFR01 | Thời gian phản hồi tra cứu | Không quá 2 giây trong điều kiện tải được quy định. |
| NFR02 | Thời gian tạo phiếu | Không quá 3 giây trong điều kiện tải được quy định. |
| NFR03 | Tính sẵn sàng | Đạt tối thiểu 99% trong khoảng thời gian đánh giá được thống nhất. |
| NFR04 | Tính duy nhất của mã phiếu | 100% phiếu được tạo có mã định danh duy nhất. |
| NFR05 | Ghi nhận lịch sử thay đổi | 100% thay đổi thuộc phạm vi theo dõi được ghi nhận. |
| NFR06 | Chuẩn hóa số điện thoại | 100% số điện thoại hợp lệ được chuẩn hóa theo quy tắc hệ thống. |

Các chỉ tiêu trên là mục tiêu đề xuất cho hệ thống. Khi triển khai và kiểm thử, cần xác định rõ môi trường đo, điều kiện tải và phạm vi đánh giá.

## 6. Truy vết yêu cầu

### 6.1. Bảng truy vết User Story – Use Case – Functional Requirement

| User Story | Use Case | Functional Requirement |
|---|---|---|
| US01 – Tra cứu khách hàng | UC01 – Tra cứu khách hàng | FR01 |
| US02 – Tạo hồ sơ khách hàng | UC02 – Tạo hồ sơ khách hàng | FR02 |
| US03 – Ghi nhận thiết bị | UC03 – Ghi nhận thiết bị | FR03 |
| US04 – Kiểm tra tình trạng bảo hành | UC04 – Kiểm tra tình trạng bảo hành | FR04 |
| US05 – Tạo phiếu bảo hành | UC05 – Tạo phiếu bảo hành | FR05 |
| US06 – Ghi nhận mô tả lỗi | UC06 – Ghi nhận mô tả lỗi | FR06 |
| US07 – Phân loại nhóm sự cố | UC07 – Phân loại nhóm sự cố | FR07 |
| US08 – Xác định mức ưu tiên | UC08 – Xác định mức ưu tiên | FR08 |
| US09 – Sinh hạn cam kết | UC09 – Sinh hạn cam kết | FR09 |

### 6.2. Quan hệ giữa các Use Case

UC05 – Tạo phiếu bảo hành là Use Case trung tâm, sử dụng các thông tin đã được xử lý từ những Use Case liên quan:

- UC01 và UC02 cung cấp thông tin khách hàng.
- UC03 cung cấp thông tin thiết bị.
- UC04 cung cấp tình trạng bảo hành.
- UC06 cung cấp mô tả lỗi.
- UC07 cung cấp nhóm sự cố.
- UC08 cung cấp mức ưu tiên.
- UC09 xác định hạn cam kết xử lý.

Các quan hệ trên thể hiện sự phụ thuộc về dữ liệu và trình tự nghiệp vụ. Khi xây dựng sơ đồ Use Case, chỉ sử dụng quan hệ `include` hoặc `extend` khi có căn cứ rõ ràng từ đặc tả nghiệp vụ.

## 7. Giả định và ràng buộc

- Số điện thoại là thông tin chính để tra cứu khách hàng.
- Serial hoặc IMEI được sử dụng để xác định thiết bị.
- Danh mục nhóm sự cố và mức ưu tiên phải được cấu hình trước khi sử dụng.
- Việc xác minh bảo hành phải tuân theo quy định nghiệp vụ của hệ thống.
- Thời hạn SLA theo từng mức ưu tiên cần được xác nhận trước khi triển khai.
- Hệ thống cần ngăn chặn việc tạo hồ sơ khách hàng trùng theo số điện thoại đã chuẩn hóa.
- Hệ thống cần đảm bảo mã phiếu bảo hành không bị trùng.
- Các API trong tài liệu là đề xuất thiết kế, không khẳng định là API đã được triển khai thực tế.

## 8. API Contract – Track SE

### 8.1. Mục đích

API Contract mô tả các giao tiếp API dự kiến phục vụ Luồng L2 – Tiếp nhận và phân loại yêu cầu bảo hành của hệ thống Smart CRM Mekong Mobile.

Các API được đề xuất hỗ trợ tra cứu khách hàng, tạo hồ sơ khách hàng, tra cứu thiết bị và tạo phiếu bảo hành. Đây là thiết kế phục vụ phân tích và phát triển hệ thống, không phải xác nhận về API thực tế của Mekong Mobile.

### 8.2. API 1 – Tra cứu khách hàng

**Method:** `GET`

**Endpoint:**

`/api/customers?phone={phone}`

**Mục đích:** Tra cứu hồ sơ khách hàng bằng số điện thoại.

**Response thành công – HTTP 200**

```json
{
  "customer_id": 1001,
  "full_name": "Nguyen Van An",
  "phone": "0901234567"
}
```

**Response không tìm thấy – HTTP 404**

```json
{
  "error": "CUSTOMER_NOT_FOUND",
  "message": "Không tìm thấy hồ sơ khách hàng."
}
```

**Quy tắc xử lý:**

- Kiểm tra số điện thoại đầu vào.
- Trả về hồ sơ tương ứng nếu tìm thấy.
- Trả về mã lỗi `CUSTOMER_NOT_FOUND` nếu không tìm thấy hồ sơ.

### 8.3. API 2 – Tạo hồ sơ khách hàng

**Method:** `POST`

**Endpoint:**

`/api/customers`

**Mục đích:** Tạo hồ sơ khách hàng mới.

**Request Body**

```json
{
  "full_name": "Nguyen Van An",
  "phone": "0901234567",
  "email": "an@example.com"
}
```

**Response thành công – HTTP 201**

```json
{
  "customer_id": 1001,
  "full_name": "Nguyen Van An",
  "phone": "0901234567"
}
```

**Response xung đột dữ liệu – HTTP 409**

```json
{
  "error": "CUSTOMER_ALREADY_EXISTS",
  "message": "Số điện thoại đã được đăng ký."
}
```

**Quy tắc xử lý:**

- Họ tên và số điện thoại phải hợp lệ.
- Số điện thoại được chuẩn hóa trước khi lưu.
- Không tạo hồ sơ mới nếu số điện thoại đã tồn tại.

### 8.4. API 3 – Tra cứu thiết bị

**Method:** `GET`

**Endpoint tra cứu bằng serial:**

`/api/devices?serial_no={serial_no}`

**Mục đích:** Tra cứu thiết bị bằng serial. Nếu tra cứu bằng IMEI, API có thể sử dụng tham số `imei` theo thiết kế thống nhất.

**Response thành công – HTTP 200**

```json
{
  "device_id": 501,
  "customer_id": 1001,
  "serial_no": "SN20260001",
  "purchase_date": "2026-01-15"
}
```

**Response không tìm thấy – HTTP 404**

```json
{
  "error": "DEVICE_NOT_FOUND",
  "message": "Không tìm thấy thiết bị."
}
```

**Quy tắc xử lý:**

- Tra cứu thiết bị theo serial hoặc IMEI.
- Trả về thông tin thiết bị và khách hàng liên quan nếu tìm thấy.
- Yêu cầu xác minh khi phát hiện thiết bị đang liên kết với khách hàng khác.

### 8.5. API 4 – Tạo phiếu bảo hành

**Method:** `POST`

**Endpoint:**

`/api/tickets`

**Mục đích:** Tạo phiếu bảo hành sau khi đã xác định thông tin khách hàng, thiết bị và nội dung yêu cầu.

**Request Body**

```json
{
  "customer_id": 1001,
  "device_id": 501,
  "description": "Máy không sạc được",
  "issue_category": "SAC",
  "priority": "CAO"
}
```

**Response thành công – HTTP 201**

```json
{
  "ticket_code": "BH-000123",
  "status": "MOI",
  "priority": "CAO",
  "commitment_deadline": "2026-10-12T17:00:00+07:00"
}
```

**Response dữ liệu không hợp lệ – HTTP 400**

```json
{
  "error": "INVALID_TICKET_DATA",
  "message": "Thông tin tạo phiếu không hợp lệ."
}
```

**Quy tắc xử lý:**

- Khách hàng và thiết bị phải tồn tại.
- Mô tả lỗi và nhóm sự cố phải đáp ứng các điều kiện bắt buộc.
- Mức ưu tiên phải thuộc danh mục được hỗ trợ.
- Hệ thống sinh mã phiếu duy nhất.
- Hệ thống xác định hạn cam kết theo quy tắc SLA đã cấu hình.
- Nếu dữ liệu không hợp lệ, hệ thống trả về thông báo lỗi tương ứng.

*Lưu ý: `commitment_deadline` trong ví dụ chỉ minh họa định dạng dữ liệu. Hạn cam kết thực tế phụ thuộc vào quy tắc SLA và lịch làm việc đã được thống nhất.*

### 8.6. Quy ước chung

| Nội dung | Quy ước |
|---|---|
| Định dạng dữ liệu | JSON |
| Giao thức | HTTP API |
| HTTP 200 | Xử lý thành công. |
| HTTP 201 | Tạo dữ liệu thành công. |
| HTTP 400 | Dữ liệu đầu vào không hợp lệ. |
| HTTP 404 | Không tìm thấy dữ liệu. |
| HTTP 409 | Xung đột dữ liệu. |

## 9. Kết luận

Tài liệu SRS rút gọn xác định phạm vi nghiệp vụ L2 – Tiếp nhận và phân loại yêu cầu bảo hành của Smart CRM Mekong Mobile, bao gồm 9 User Story, 9 Use Case, 9 yêu cầu chức năng và 6 yêu cầu phi chức năng.

Bảng truy vết giúp liên kết User Story với Use Case và yêu cầu chức năng tương ứng. Phần đặc tả UC05 làm rõ quy trình tạo phiếu bảo hành, các điều kiện tiên quyết, luồng xử lý chính và các trường hợp ngoại lệ.

API Contract cung cấp cơ sở thiết kế giao tiếp giữa các thành phần hệ thống, phục vụ các bước thiết kế cơ sở dữ liệu, xây dựng giao diện và phát triển phần mềm trong giai đoạn tiếp theo.