
import re

from src.repositories.customer_repository import (
    find_by_phone,
    create_customer,
)


def get_customer_by_phone(phone: str):
    phone = phone.strip()

    if not re.fullmatch(r"[0-9+]{9,15}", phone):
        raise ValueError("Số điện thoại không hợp lệ")

    customer = find_by_phone(phone)

    if customer is None:
        return None

    return {
        "customer_id": f"CUS{customer['customer_id']:03d}",
        "customer_name": customer["full_name"],
        "phone": customer["phone"],
    }


def add_customer(
    customer_name: str,
    phone: str,
    email: str = None,
    address: str = None,
):
    customer_name = customer_name.strip()
    phone = phone.strip()

    if not customer_name:
        raise ValueError("Tên khách hàng không được để trống")

    if not re.fullmatch(r"[0-9+]{9,15}", phone):
        raise ValueError("Số điện thoại không hợp lệ")

    if email is not None:
        email = email.strip() or None

    if address is not None:
        address = address.strip() or None

    if find_by_phone(phone) is not None:
        raise ValueError("Số điện thoại đã tồn tại")

    return create_customer(
        customer_name,
        phone,
        email,
        address,
    )
