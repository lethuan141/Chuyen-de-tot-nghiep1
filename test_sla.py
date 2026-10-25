
from datetime import datetime

import pytest

from src.services.ticket_service import (
    add_working_hours,
    SLA_BY_PRIORITY,
)


def test_sla_priorities_are_configured():
    assert SLA_BY_PRIORITY == {
        "CAO": 24,
        "TRUNG_BINH": 72,
        "THAP": 120,
    }


def test_add_hours_during_morning():
    start = datetime(2026, 10, 19, 9, 0)
    assert add_working_hours(start, 2) == datetime(2026, 10, 19, 11, 0)


def test_add_hours_skips_lunch_break():
    start = datetime(2026, 10, 19, 11, 0)
    assert add_working_hours(start, 2) == datetime(2026, 10, 19, 14, 0)


def test_add_hours_skips_weekend():
    start = datetime(2026, 10, 23, 16, 0)  # Friday
    assert add_working_hours(start, 2) == datetime(2026, 10, 26, 9, 0)


def test_start_before_working_hours():
    start = datetime(2026, 10, 19, 7, 0)
    assert add_working_hours(start, 1) == datetime(2026, 10, 19, 9, 0)


def test_zero_hours_returns_start():
    start = datetime(2026, 10, 19, 9, 0)
    assert add_working_hours(start, 0) == start
