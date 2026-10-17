
from src.db import get_connection


def find_by_serial(serial_no: str):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    d.device_id,
                    d.customer_id,
                    c.full_name AS customer_name,
                    c.phone,
                    d.device_type,
                    d.brand,
                    d.model,
                    d.serial_number,
                    d.warranty_end_date
                FROM devices d
                JOIN customers c
                    ON d.customer_id = c.customer_id
                WHERE d.serial_number = %s
                """,
                (serial_no,),
            )
            return cursor.fetchone()
    finally:
        connection.close()
