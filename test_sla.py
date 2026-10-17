
from datetime import datetime

from src.services.ticket_service import (
    add_working_hours,
    SLA_BY_PRIORITY,
)

start = datetime(2026, 10, 19, 9, 0)  # Thứ Hai, 09:00

for priority, hours in SLA_BY_PRIORITY.items():
    deadline = add_working_hours(start, hours)
    print(f"{priority}: {hours} giờ làm việc")
    print(f"  Bắt đầu: {start}")
    print(f"  Hạn cam kết: {deadline}")
    print()
