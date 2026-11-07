# TEST REPORT – SMART CRM MEKONG MOBILE



## 1. Thông tin chung



- **Dự án:** Smart CRM – Mekong Mobile

- **Luồng nghiệp vụ:** L2 – Tiếp nhận và phân loại yêu cầu bảo hành

- **Loại tài liệu:** Test Report

- **Phiên bản:** 1.0

- **Ngày kiểm thử:** 07/11/2026

- **Công cụ:** Python, Pytest

- **File kiểm thử:** `test\_customer\_device.py`



## 2. Mục tiêu kiểm thử



Ghi nhận kết quả thực tế của bộ kiểm thử nhằm đánh giá chức năng quản lý khách hàng, quản lý thiết bị và khả năng xử lý dữ liệu hợp lệ, không hợp lệ trong hệ thống Smart CRM.



## 3. Môi trường kiểm thử



- Hệ điều hành: Windows.

- Ngôn ngữ: Python.

- Framework Backend: FastAPI.

- Cơ sở dữ liệu: MySQL.

- Công cụ kiểm thử: Pytest.

- Thư mục lưu ảnh: `docs/screenshots/`.



## 4. Kết quả kiểm thử tổng hợp



Theo kết quả chạy thực tế ngày 07/11/2026:



| Nội dung | Kết quả |

|---|---:|

| Tổng số Test Case | 18 |

| Số PASS | 18 |

| Số FAIL | 0 |

| Tỷ lệ PASS | 100% |

| Thời gian chạy | 0.11 giây |



**Lệnh kiểm thử toàn bộ:**



```cmd

python -m pytest -v

```



## 5. Kết quả kiểm thử bổ sung TC-15 đến TC-18



| Test Case | Nội dung | Kết quả |

|---|---|---|

| TC-15 | Kiểm tra số điện thoại trùng | PASS |

| TC-16 | Kiểm tra ngày hết hạn trước ngày mua | PASS |

| TC-17 | Kiểm tra SQL Injection | PASS |

| TC-18 | Kiểm tra truy vấn SQL tham số | PASS |



Các Test Case trên đã được thực thi bằng Pytest và cho kết quả PASS.



Lưu ý: TC-17 kiểm tra khả năng xử lý đầu vào SQL Injection tại Service. TC-18 kiểm tra việc truyền tham số SQL bằng mock Repository. Đây không phải kiểm thử xâm nhập toàn diện trên hệ thống thực tế.



## 6. Đánh giá theo 5 loại kiểm thử



| Loại kiểm thử | Nội dung | Đánh giá |

|---|---|---|

| Luồng đúng | Kiểm tra nghiệp vụ với dữ liệu hợp lệ | Có |

| Giá trị biên | Kiểm tra giới hạn dữ liệu | Có |

| Dữ liệu sai | Kiểm tra dữ liệu không hợp lệ | Có |

| Bảo mật/chất lượng dữ liệu | TC-15, TC-17, TC-18 | Có |

| Tái lập | Chạy lại toàn bộ bộ kiểm thử | Có kết quả chạy lại |



## 7. Minh chứng kiểm thử



Ảnh chụp kết quả được lưu trong thư mục `docs/screenshots/`.



| Tên ảnh | Nội dung |

|---|---|

| `TC-15-18.png` | Kết quả kiểm thử 4 Test Case bổ sung |

| `full-suite-01.png` | Kết quả chạy toàn bộ bộ kiểm thử |

| `full-suite-02.png` | Kết quả chạy lại toàn bộ bộ kiểm thử |

| `test-run-01.png` | Minh chứng lần chạy kiểm thử |

| `test-run-02.png` | Minh chứng lần chạy kiểm thử |



## 8. Đánh giá chung



Bộ kiểm thử ghi nhận 18/18 Test Case PASS, không có Test Case FAIL trong các lần chạy được báo cáo.



Các ảnh chụp kết quả được lưu trong thư mục minh chứng để phục vụ việc đối chiếu.



## 9. Kết luận



Kết quả kiểm thử hiện tại cho thấy các Test Case đã thực hiện đều đáp ứng kết quả mong đợi.



Bộ kiểm thử có thể được thực hiện lại bằng lệnh:



```cmd

python -m pytest -v

```



Các kết quả được sử dụng làm minh chứng cho quá trình kiểm thử và hoàn thiện dự án Smart CRM – Mekong Mobile.

