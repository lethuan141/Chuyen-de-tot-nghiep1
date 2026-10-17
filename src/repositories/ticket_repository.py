
from datetime import datetime

from src.db import get_connection


def create_ticket(
    ticket_code: str,
    customer_id: int,
    device_id: int,
    received_by: int,
    issue_type_id: int,
    priority_id: int,
    description: str,
    commitment_at,
):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            # Tạo phiếu với mã tạm duy nhất
            cursor.execute(
                """
                INSERT INTO warranty_tickets (
                    ticket_code,
                    customer_id,
                    device_id,
                    received_by,
                    issue_type_id,
                    priority_id,
                    description,
                    status,
                    commitment_at
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    f"TEMP-{customer_id}-{device_id}-{datetime.now().strftime('%Y%m%d%H%M%S%f')}",
                    customer_id,
                    device_id,
                    received_by,
                    issue_type_id,
                    priority_id,
                    description,
                    "MỚI",
                    commitment_at,
                ),
            )

            ticket_id = cursor.lastrowid

            # Mã chính thức: BH-YYYYMMDD-XXXX
            ticket_date = datetime.now().strftime("%Y%m%d")
            final_code = f"BH-{ticket_date}-{ticket_id:04d}"

            cursor.execute(
                """
                UPDATE warranty_tickets
                SET ticket_code = %s
                WHERE ticket_id = %s
                """,
                (final_code, ticket_id),
            )

        connection.commit()

        return {
            "ticket_id": ticket_id,
            "ticket_code": final_code,
            "status": "MỚI",
            "commitment_deadline": commitment_at.isoformat(
                sep=" ",
                timespec="seconds",
            ),
        }

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def get_ticket_options(issue_type_name: str, priority_name: str):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT issue_type_id, default_sla_hours
                FROM issue_types
                WHERE name = %s
                """,
                (issue_type_name,),
            )
            issue_type = cursor.fetchone()

            cursor.execute(
                """
                SELECT priority_id
                FROM priorities
                WHERE name = %s
                """,
                (priority_name,),
            )
            priority = cursor.fetchone()

            return issue_type, priority

    finally:
        connection.close()


def customer_and_device_exist(
    customer_id: int,
    device_id: int,
):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT 1
                FROM devices
                WHERE device_id = %s
                  AND customer_id = %s
                """,
                (device_id, customer_id),
            )

            return cursor.fetchone() is not None

    finally:
        connection.close()
