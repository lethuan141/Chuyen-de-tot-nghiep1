
from datetime import date

from src.repositories.device_repository import (
    find_by_serial,
    get_all_devices,
    find_by_id,
    create_device,
    update_device,
    delete_device,
)


def format_device(device):
    if device is None:
        return None

    return {
        "device_id": device["device_id"],
        "customer_id": device["customer_id"],
        "customer_name": device["customer_name"],
        "phone": device["phone"],
        "device_type": device["device_type"],
        "brand": device["brand"],
        "model": device["model"],
        "serial_no": device["serial_number"],
        "purchase_date": (
            device["purchase_date"].isoformat()
            if device["purchase_date"]
            else None
        ),
        "warranty_end_date": (
            device["warranty_end_date"].isoformat()
            if device["warranty_end_date"]
            else None
        ),
    }


def validate_date(value, field_name):
    if value is None or value == "":
        return None

    if isinstance(value, date):
        return value

    if not isinstance(value, str):
        raise ValueError(f"{field_name} phải có định dạng YYYY-MM-DD")

    value = value.strip()

    try:
        parsed_date = date.fromisoformat(value)
    except ValueError:
        raise ValueError(
            f"{field_name} không hợp lệ, vui lòng nhập theo YYYY-MM-DD"
        )

    if parsed_date.isoformat() != value:
        raise ValueError(
            f"{field_name} phải có định dạng YYYY-MM-DD"
        )

    return parsed_date


def validate_device(
    customer_id,
    device_type,
    brand,
    model,
    serial_no,
):
    if not isinstance(customer_id, int) or customer_id <= 0:
        raise ValueError("Customer ID phải là số nguyên dương")

    fields = {
        "Loại thiết bị": (device_type, 80),
        "Thương hiệu": (brand, 100),
        "Model": (model, 100),
        "Serial/IMEI": (serial_no, 100),
    }

    validated = {}

    for field_name, (value, max_length) in fields.items():
        if not isinstance(value, str):
            raise ValueError(f"{field_name} phải là chuỗi")

        value = value.strip()

        if not value:
            raise ValueError(f"{field_name} không được để trống")

        if len(value) > max_length:
            raise ValueError(
                f"{field_name} không được vượt quá {max_length} ký tự"
            )

        validated[field_name] = value

    return (
        validated["Loại thiết bị"],
        validated["Thương hiệu"],
        validated["Model"],
        validated["Serial/IMEI"],
    )


def validate_device_dates(purchase_date, warranty_end_date):
    purchase_date = validate_date(
        purchase_date,
        "Ngày mua",
    )

    warranty_end_date = validate_date(
        warranty_end_date,
        "Ngày hết hạn bảo hành",
    )

    if (
        purchase_date is not None
        and warranty_end_date is not None
        and warranty_end_date < purchase_date
    ):
        raise ValueError(
            "Ngày hết hạn bảo hành không được trước ngày mua"
        )

    return purchase_date, warranty_end_date


def get_device_by_serial(serial_no: str):
    if not isinstance(serial_no, str):
        raise ValueError("Serial/IMEI không hợp lệ")

    serial_no = serial_no.strip()

    if not serial_no:
        raise ValueError("Serial/IMEI không được để trống")

    device = find_by_serial(serial_no)

    return format_device(device)


def get_devices():
    return [
        format_device(device)
        for device in get_all_devices()
    ]


def get_device(device_id):
    if not isinstance(device_id, int) or device_id <= 0:
        raise ValueError("Device ID phải là số nguyên dương")

    return format_device(find_by_id(device_id))


def add_device(
    customer_id,
    device_type,
    brand,
    model,
    serial_no,
    purchase_date=None,
    warranty_end_date=None,
):
    (
        device_type,
        brand,
        model,
        serial_no,
    ) = validate_device(
        customer_id,
        device_type,
        brand,
        model,
        serial_no,
    )

    purchase_date, warranty_end_date = validate_device_dates(
        purchase_date,
        warranty_end_date,
    )

    device = create_device(
        customer_id,
        device_type,
        brand,
        model,
        serial_no,
        purchase_date,
        warranty_end_date,
    )

    return format_device(device)


def edit_device(
    device_id,
    customer_id,
    device_type,
    brand,
    model,
    serial_no,
    purchase_date=None,
    warranty_end_date=None,
):
    if not isinstance(device_id, int) or device_id <= 0:
        raise ValueError("Device ID phải là số nguyên dương")

    if find_by_id(device_id) is None:
        return None

    (
        device_type,
        brand,
        model,
        serial_no,
    ) = validate_device(
        customer_id,
        device_type,
        brand,
        model,
        serial_no,
    )

    purchase_date, warranty_end_date = validate_device_dates(
        purchase_date,
        warranty_end_date,
    )

    updated = update_device(
        device_id,
        customer_id,
        device_type,
        brand,
        model,
        serial_no,
        purchase_date,
        warranty_end_date,
    )

    if not updated:
        return None

    return get_device(device_id)


def remove_device(device_id):
    if not isinstance(device_id, int) or device_id <= 0:
        raise ValueError("Device ID phải là số nguyên dương")

    if find_by_id(device_id) is None:
        return False

    return delete_device(device_id)
