
import re

from src.repositories.customer_repository import (
    find_by_phone,
    create_customer,
    get_all_customers,
    find_by_id,
    update_customer,
    delete_customer,
)


def format_customer(customer):
    if customer is None:
        return None

    customer_id = customer["customer_id"]

    return {
        "customer_id": customer_id,
        "customer_code": customer.get(
            "customer_code", f"CUS{customer_id:03d}"
        ),
        "customer_name": customer.get(
            "full_name", customer.get("customer_name")
        ),
        "phone": customer.get("phone"),
        "email": customer.get("email"),
        "address": customer.get("address"),
    }


def validate_customer(customer_name, phone):
    if not isinstance(customer_name, str):
        raise ValueError("Tên khách hàng không hợp lệ")

    if not isinstance(phone, str):
        raise ValueError("Số điện thoại không hợp lệ")

    customer_name = customer_name.strip()
    phone = phone.strip()

    if not customer_name:
        raise ValueError("Tên khách hàng không được để trống")

    if not re.fullmatch(r"[0-9+]{9,15}", phone):
        raise ValueError("Số điện thoại không hợp lệ")

    return customer_name, phone


def get_customer_by_phone(phone: str):
    if not isinstance(phone, str):
        raise ValueError("Số điện thoại không hợp lệ")

    phone = phone.strip()

    if not re.fullmatch(r"[0-9+]{9,15}", phone):
        raise ValueError("Số điện thoại không hợp lệ")

    return format_customer(find_by_phone(phone))


def add_customer(customer_name, phone, email=None, address=None):
    customer_name, phone = validate_customer(customer_name, phone)

    if email is not None:
        email = email.strip() or None

    if address is not None:
        address = address.strip() or None

    if find_by_phone(phone) is not None:
        raise ValueError("Số điện thoại đã tồn tại")

    result = create_customer(
        customer_name,
        phone,
        email,
        address
    )

    if result is None:
        return None

    customer_data = {
        "customer_id": result["customer_id"],
        "customer_code": result.get("customer_code"),
        "customer_name": customer_name,
        "phone": phone,
        "email": email,
        "address": address,
    }

    return format_customer(customer_data)


def get_customers():
    return [
        format_customer(customer)
        for customer in get_all_customers()
    ]


def get_customer(customer_id):
    customer = find_by_id(customer_id)

    if customer is None:
        return None

    return format_customer(customer)


def edit_customer(
    customer_id,
    customer_name,
    phone,
    email=None,
    address=None
):
    customer_name, phone = validate_customer(customer_name, phone)

    existing = find_by_id(customer_id)

    if existing is None:
        return None

    customer_with_phone = find_by_phone(phone)

    if (
        customer_with_phone is not None
        and customer_with_phone["customer_id"] != customer_id
    ):
        raise ValueError("Số điện thoại đã tồn tại")

    if email is not None:
        email = email.strip() or None

    if address is not None:
        address = address.strip() or None

    updated = update_customer(
        customer_id,
        customer_name,
        phone,
        email,
        address
    )

    if not updated:
        return None

    return get_customer(customer_id)


def remove_customer(customer_id):
    if find_by_id(customer_id) is None:
        return False

    return delete_customer(customer_id)
