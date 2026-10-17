
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from src.services.ticket_service import add_ticket

router = APIRouter(prefix="/api/tickets", tags=["Tickets"])


class TicketCreate(BaseModel):
    customer_id: int = Field(gt=0)
    device_id: int = Field(gt=0)
    issue_description: str = Field(min_length=1)
    issue_category: str
    priority: str


@router.post("", status_code=201)
def create_ticket_api(data: TicketCreate):
    try:
        return add_ticket(
            customer_id=data.customer_id,
            device_id=data.device_id,
            description=data.issue_description,
            issue_category=data.issue_category,
            priority=data.priority,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi tạo phiếu bảo hành",
        )
