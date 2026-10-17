
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from src.services.customer_service import (
    get_customer_by_phone,
    add_customer,
)

router = APIRouter(prefix="/api/customers", tags=["Customers"])


class CustomerCreate(BaseModel):
    customer_name: str = Field(min_length=1, max_length=150)
    phone: str = Field(min_length=9, max_length=15)
    email: str | None = None
    address: str | None = None


@router.get("")
def lookup_customer(phone: str = Query(..., min_length=1)):
    try:
        customer = get_customer_by_phone(phone)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi kết nối hoặc truy vấn cơ sở dữ liệu",
        )

    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    return customer


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
    except Exception:
        raise HTTPException(status_code=500, detail="Lỗi tạo khách hàng")
