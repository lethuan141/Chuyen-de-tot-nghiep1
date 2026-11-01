
from src.db import get_connection


def find_by_phone(phone: str):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT customer_id, full_name, phone
                FROM customers
                WHERE phone = %s
                """,
                (phone,),
            )
            return cursor.fetchone()
    finally:
        connection.close()


def create_customer(
    customer_name: str,
    phone: str,
    email: str = None,
    address: str = None,
):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO customers
                    (full_name, phone, email, address)
                VALUES (%s, %s, %s, %s)
                """,
                (customer_name, phone, email, address),
            )
            customer_id = cursor.lastrowid

        connection.commit()
        return {
            "customer_id": customer_id,
            "customer_code": f"CUS{customer_id:03d}",
            "customer_name": customer_name,
            "phone": phone,
            "email": email,
            "address": address,
        }
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def get_all_customers():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT customer_id, full_name, phone, email, address
                FROM customers
                ORDER BY customer_id DESC
                """
            )
            return cursor.fetchall()
    finally:
        connection.close()


def find_by_id(customer_id: int):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT customer_id, full_name, phone, email, address
                FROM customers
                WHERE customer_id = %s
                """,
                (customer_id,),
            )
            return cursor.fetchone()
    finally:
        connection.close()


def update_customer(
    customer_id: int,
    customer_name: str,
    phone: str,
    email: str = None,
    address: str = None,
):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE customers
                SET full_name = %s, phone = %s,
                    email = %s, address = %s
                WHERE customer_id = %s
                """,
                (customer_name, phone, email, address, customer_id),
            )
            updated = cursor.rowcount > 0

        connection.commit()
        return updated
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


def delete_customer(customer_id: int):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM customers WHERE customer_id = %s",
                (customer_id,),
            )
            deleted = cursor.rowcount > 0

        connection.commit()
        return deleted
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
