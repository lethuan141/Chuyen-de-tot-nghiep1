
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
def get_all_tickets():
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    wt.ticket_id,
                    wt.ticket_code,
                    wt.customer_id,
                    c.full_name AS customer_name,
                    wt.device_id,
                    d.serial_number,
                    it.name AS issue_category,
                    p.name AS priority,
                    wt.description,
                    wt.status,
                    wt.received_at,
                    wt.commitment_at
                FROM warranty_tickets wt
                JOIN customers c
                    ON wt.customer_id = c.customer_id
                JOIN devices d
                    ON wt.device_id = d.device_id
                JOIN issue_types it
                    ON wt.issue_type_id = it.issue_type_id
                JOIN priorities p
                    ON wt.priority_id = p.priority_id
                ORDER BY wt.ticket_id DESC
            """)

            return cursor.fetchall()

    finally:
        connection.close()


def get_ticket_by_id(ticket_id: int):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    wt.ticket_id,
                    wt.ticket_code,
                    wt.customer_id,
                    c.full_name AS customer_name,
                    wt.device_id,
                    d.serial_number,
                    it.name AS issue_category,
                    p.name AS priority,
                    wt.description,
                    wt.status,
                    wt.received_at,
                    wt.commitment_at
                FROM warranty_tickets wt
                JOIN customers c
                    ON wt.customer_id = c.customer_id
                JOIN devices d
                    ON wt.device_id = d.device_id
                JOIN issue_types it
                    ON wt.issue_type_id = it.issue_type_id
                JOIN priorities p
                    ON wt.priority_id = p.priority_id
                WHERE wt.ticket_id = %s
            """, (ticket_id,))

            return cursor.fetchone()

    finally:
        connection.close()

def update_ticket(
    ticket_id: int,
    description: str,
    issue_type_id: int,
    priority_id: int,
    commitment_at,
):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE warranty_tickets
                SET description = %s,
                    issue_type_id = %s,
                    priority_id = %s,
                    commitment_at = %s
                WHERE ticket_id = %s
                """,
                (
                    description,
                    issue_type_id,
                    priority_id,
                    commitment_at,
                    ticket_id,
                ),
            )

            updated = cursor.rowcount > 0

        connection.commit()
        return updated

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def delete_ticket(ticket_id: int):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            # Kiểm tra phiếu có tồn tại không
            cursor.execute(
                """
                SELECT ticket_id
                FROM warranty_tickets
                WHERE ticket_id = %s
                """,
                (ticket_id,),
            )

            if cursor.fetchone() is None:
                return False

            # Không xóa nếu phiếu đã có lịch sử trạng thái
            cursor.execute(
                """
                SELECT history_id
                FROM ticket_status_history
                WHERE ticket_id = %s
                LIMIT 1
                """,
                (ticket_id,),
            )

            if cursor.fetchone() is not None:
                raise ValueError(
                    "Không thể xóa phiếu đã có lịch sử trạng thái"
                )

            cursor.execute(
                """
                DELETE FROM warranty_tickets
                WHERE ticket_id = %s
                """,
                (ticket_id,),
            )

        connection.commit()
        return True

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
