
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
            "customer_id": f"CUS{customer_id:03d}",
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
