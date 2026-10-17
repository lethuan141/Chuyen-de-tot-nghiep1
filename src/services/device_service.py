
from src.repositories.device_repository import find_by_serial


def get_device_by_serial(serial_no: str):
    serial_no = serial_no.strip()

    if not serial_no:
        raise ValueError("Serial/IMEI không được để trống")

    device = find_by_serial(serial_no)

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
        "warranty_end_date": (
            device["warranty_end_date"].isoformat()
            if device["warranty_end_date"]
            else None
        ),
    }
