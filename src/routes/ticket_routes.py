
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from src.services.ticket_service import (
    add_ticket,
    list_tickets,
    find_ticket,
    edit_ticket,
    remove_ticket,
)
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


@router.get("")
def get_tickets_api():
    return list_tickets()


@router.get("/{ticket_id}")
def get_ticket_api(ticket_id: int):
    try:
        ticket = find_ticket(ticket_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail="Không tìm thấy phiếu bảo hành",
        )

    return ticket

class TicketUpdate(BaseModel):
    issue_description: str = Field(min_length=1)
    issue_category: str = Field(min_length=1)
    priority: str = Field(min_length=1)


@router.put("/{ticket_id}")
def update_ticket_api(ticket_id: int, data: TicketUpdate):
    try:
        return edit_ticket(
            ticket_id=ticket_id,
            description=data.issue_description,
            issue_category=data.issue_category,
            priority=data.priority,
        )
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi cập nhật phiếu bảo hành",
        )

@router.delete("/{ticket_id}")
def delete_ticket_api(ticket_id: int):
    try:
        return remove_ticket(ticket_id)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error))
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi xóa phiếu bảo hành",
        )
