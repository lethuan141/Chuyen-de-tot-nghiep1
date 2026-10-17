
from fastapi import APIRouter, HTTPException, Query

from src.services.device_service import get_device_by_serial

router = APIRouter(prefix="/api/devices", tags=["Devices"])


@router.get("")
def lookup_device(serial_no: str = Query(..., min_length=1)):
    try:
        device = get_device_by_serial(serial_no)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi truy vấn thiết bị",
        )

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device
