
import pytest

from src.services import customer_service, device_service


# =========================
# CUSTOMER - HAPPY PATH
# =========================

def test_add_customer_happy_path(monkeypatch):
    monkeypatch.setattr(
        customer_service, "find_by_phone", lambda phone: None
    )
    monkeypatch.setattr(
        customer_service,
        "create_customer",
        lambda *args: {"customer_id": 10}
    )

    result = customer_service.add_customer(
        "Nguyen Van A", "0912345678"
    )

    assert result["customer_id"] == 10


# =========================
# CUSTOMER - BOUNDARY VALUE
# =========================

@pytest.mark.parametrize(
    "phone",
    ["123456789", "123456789012345"]
)
def test_customer_phone_boundary(phone):
    name, valid_phone = customer_service.validate_customer(
        "Nguyen Van A", phone
    )

    assert name == "Nguyen Van A"
    assert valid_phone == phone


# =========================
# CUSTOMER - INVALID DATA
# =========================

def test_customer_rejects_invalid_phone():
    with pytest.raises(ValueError):
        customer_service.validate_customer(
            "Nguyen Van A", "12345678"
        )


def test_customer_rejects_empty_name():
    with pytest.raises(ValueError):
        customer_service.validate_customer(
            "   ", "0912345678"
        )


# =========================
# DEVICE - HAPPY PATH
# =========================

def test_device_validation_happy_path():
    result = device_service.validate_device(
        1,
        " Smartphone ",
        " Apple ",
        " iPhone 15 ",
        " IMEI123456789 "
    )

    assert result == (
        "Smartphone",
        "Apple",
        "iPhone 15",
        "IMEI123456789"
    )


# =========================
# DEVICE - INVALID DATA
# =========================

def test_device_rejects_missing_customer():
    with pytest.raises(ValueError):
        device_service.validate_device(
            None, "Smartphone", "Apple",
            "iPhone 15", "IMEI123456789"
        )


def test_device_rejects_empty_brand():
    with pytest.raises(ValueError):
        device_service.validate_device(
            1, "Smartphone", " ",
            "iPhone 15", "IMEI123456789"
        )

# =========================
# TC-15 - DUPLICATE CUSTOMER PHONE
# =========================

def test_TC15_reject_duplicate_customer_phone(monkeypatch):
    monkeypatch.setattr(
        customer_service,
        "find_by_phone",
        lambda phone: {"customer_id": 1, "phone": phone}
    )

    with pytest.raises(ValueError, match="Số điện thoại đã tồn tại"):
        customer_service.add_customer(
            "Nguyen Van B", "0912345678"
        )


# =========================
# TC-16 - INVALID WARRANTY DATE
# =========================

def test_TC16_reject_warranty_before_purchase():
    with pytest.raises(
        ValueError,
        match="không được trước ngày mua"
    ):
        device_service.validate_device_dates(
            "2026-10-20",
            "2026-10-19"
        )


# =========================
# TC-17 - SQL INJECTION INPUT
# =========================

def test_TC17_reject_sql_injection_phone():
    malicious_phone = "0912345678' OR '1'='1"

    with pytest.raises(ValueError, match="Số điện thoại không hợp lệ"):
        customer_service.validate_customer(
            "Nguyen Van A",
            malicious_phone
        )


# =========================
# TC-18 - PARAMETERIZED SQL QUERY
# =========================

def test_TC18_device_repository_uses_sql_parameters(monkeypatch):
    from src.repositories import device_repository

    captured = {}

    class FakeCursor:
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_value, traceback):
            return False

        def execute(self, query, params=None):
            captured["query"] = query
            captured["params"] = params

        def fetchone(self):
            return None

    class FakeConnection:
        def cursor(self):
            return FakeCursor()

        def close(self):
            pass

    monkeypatch.setattr(
        device_repository,
        "get_connection",
        lambda: FakeConnection()
    )

    malicious_serial = "IMEI' OR '1'='1"

    device_repository.find_by_serial(malicious_serial)

    assert "WHERE d.serial_number = %s" in captured["query"]
    assert captured["params"] == (malicious_serial,)
    assert malicious_serial not in captured["query"]
