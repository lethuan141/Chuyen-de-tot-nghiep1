
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from pymysql.err import IntegrityError

from src.services.customer_service import (
    get_customer_by_phone,
    add_customer,
    get_customers,
    get_customer,
    edit_customer,
    remove_customer,
)

router = APIRouter(prefix="/api/customers", tags=["Customers"])


class CustomerCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=150)
    phone: str = Field(min_length=9, max_length=15)
    email: str | None = None
    address: str | None = None


@router.get("")
def lookup_customer(phone: str | None = Query(None)):
    # Có phone: tra cứu khách hàng theo số điện thoại
    # Không có phone: lấy danh sách khách hàng
    try:
        if phone is None:
            return get_customers()

        customer = get_customer_by_phone(phone)

        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")

        return customer

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Database error")


@router.post("", status_code=201)
def create_customer_api(data: CustomerCreate):
    try:
        return add_customer(
            data.customer_name,
            data.phone,
            data.email,
            data.address,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Customer already exists")
    except Exception:
        raise HTTPException(status_code=500, detail="Cannot create customer")


@router.get("/{customer_id}")
def get_customer_api(customer_id: int):
    customer = get_customer(customer_id)

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer


@router.put("/{customer_id}")
def update_customer_api(customer_id: int, data: CustomerCreate):
    try:
        customer = edit_customer(
            customer_id,
            data.customer_name,
            data.phone,
            data.email,
            data.address,
        )

        if customer is None:
            raise HTTPException(status_code=404, detail="Customer not found")

        return customer

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except IntegrityError:
        raise HTTPException(status_code=409, detail="Customer data conflicts")
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Cannot update customer")


@router.delete("/{customer_id}")
def delete_customer_api(customer_id: int):
    try:
        deleted = remove_customer(customer_id)

        if not deleted:
            raise HTTPException(status_code=404, detail="Customer not found")

        return {
            "message": "Customer deleted successfully",
            "customer_id": customer_id,
        }

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Cannot delete customer because related devices or tickets exist",
        )
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500, detail="Cannot delete customer")
