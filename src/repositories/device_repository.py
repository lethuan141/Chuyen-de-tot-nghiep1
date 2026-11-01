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
                    d.purchase_date,
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


def get_all_devices():
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
                    d.purchase_date,
                    d.warranty_end_date
                FROM devices d
                JOIN customers c
                    ON d.customer_id = c.customer_id
                ORDER BY d.device_id DESC
                """
            )
            return cursor.fetchall()
    finally:
        connection.close()


def find_by_id(device_id: int):
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
                    d.purchase_date,
                    d.warranty_end_date
                FROM devices d
                JOIN customers c
                    ON d.customer_id = c.customer_id
                WHERE d.device_id = %s
                """,
                (device_id,),
            )
            return cursor.fetchone()
    finally:
        connection.close()


def create_device(
    customer_id,
    device_type,
    brand,
    model,
    serial_number,
    purchase_date,
    warranty_end_date,
):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO devices (
                    customer_id,
                    device_type,
                    brand,
                    model,
                    serial_number,
                    purchase_date,
                    warranty_end_date
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    customer_id,
                    device_type,
                    brand,
                    model,
                    serial_number,
                    purchase_date,
                    warranty_end_date,
                ),
            )

            device_id = cursor.lastrowid
            connection.commit()

            return find_by_id(device_id)

    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def update_device(
    device_id,
    customer_id,
    device_type,
    brand,
    model,
    serial_number,
    purchase_date,
    warranty_end_date,
):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE devices
                SET
                    customer_id = %s,
                    device_type = %s,
                    brand = %s,
                    model = %s,
                    serial_number = %s,
                    purchase_date = %s,
                    warranty_end_date = %s
                WHERE device_id = %s
                """,
                (
                    customer_id,
                    device_type,
                    brand,
                    model,
                    serial_number,
                    purchase_date,
                    warranty_end_date,
                    device_id,
                ),
            )

            connection.commit()
            return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def delete_device(device_id):
    connection = get_connection()

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM devices
                WHERE device_id = %s
                """,
                (device_id,),
            )

            connection.commit()
            return cursor.rowcount > 0

    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()