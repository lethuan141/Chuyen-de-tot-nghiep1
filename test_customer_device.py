
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
