
from datetime import datetime, timedelta

from src.repositories.ticket_repository import (
    create_ticket,
    get_ticket_options,
    customer_and_device_exist,
)


SLA_BY_PRIORITY = {
    "CAO": 24,
    "TRUNG_BINH": 72,
    "THAP": 120,
}


def add_working_hours(start: datetime, hours: int) -> datetime:
    """Cộng giờ làm việc, không tính giờ nghỉ trưa và cuối tuần."""
    current = start
    remaining = float(hours)

    while remaining > 0:
        if current.weekday() >= 5:
            current = (current + timedelta(days=1)).replace(
                hour=8, minute=0, second=0, microsecond=0
            )
            continue

        morning_start = current.replace(
            hour=8, minute=0, second=0, microsecond=0
        )
        lunch_start = current.replace(
            hour=12, minute=0, second=0, microsecond=0
        )
        afternoon_start = current.replace(
            hour=13, minute=0, second=0, microsecond=0
        )
        workday_end = current.replace(
            hour=17, minute=0, second=0, microsecond=0
        )

        if current < morning_start:
            current = morning_start
        elif lunch_start <= current < afternoon_start:
            current = afternoon_start
        elif current >= workday_end:
            current = (current + timedelta(days=1)).replace(
                hour=8, minute=0, second=0, microsecond=0
            )
            continue

        if current < lunch_start:
            available = (
                lunch_start - current
            ).total_seconds() / 3600

            if remaining <= available:
                return current + timedelta(hours=remaining)

            remaining -= available
            current = afternoon_start

        else:
            available = (
                workday_end - current
            ).total_seconds() / 3600

            if remaining <= available:
                return current + timedelta(hours=remaining)

            remaining -= available
            current = (current + timedelta(days=1)).replace(
                hour=8, minute=0, second=0, microsecond=0
            )

    return current


def add_ticket(
    customer_id: int,
    device_id: int,
    description: str,
    issue_category: str,
    priority: str,
    received_by: int = 1,
):
    description = description.strip()
    issue_category = issue_category.strip().upper()
    priority = priority.strip().upper()

    if not description:
        raise ValueError("Mô tả lỗi không được để trống")

    if priority not in SLA_BY_PRIORITY:
        raise ValueError("Mức ưu tiên không hợp lệ")

    if not customer_and_device_exist(customer_id, device_id):
        raise ValueError(
            "Khách hàng không tồn tại hoặc thiết bị không thuộc khách hàng"
        )

    issue_type, priority_record = get_ticket_options(
        issue_category,
        priority,
    )

    if issue_type is None:
        raise ValueError("Loại sự cố không hợp lệ")

    if priority_record is None:
        raise ValueError("Mức ưu tiên không hợp lệ")

    received_at = datetime.now()

    commitment_at = add_working_hours(
        received_at,
        SLA_BY_PRIORITY[priority],
    )

    # Repository sẽ tạo mã phiếu chính thức dựa trên ticket_id.
    ticket_code = (
        f"TEMP-{received_at:%Y%m%d%H%M%S%f}"
    )

    return create_ticket(
        ticket_code=ticket_code,
        customer_id=customer_id,
        device_id=device_id,
        received_by=received_by,
        issue_type_id=issue_type["issue_type_id"],
        priority_id=priority_record["priority_id"],
        description=description,
        commitment_at=commitment_at,
    )
