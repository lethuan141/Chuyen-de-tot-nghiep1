from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from pymysql.err import IntegrityError

from src.services.device_service import (
    get_device_by_serial,
    get_devices,
    get_device,
    add_device,
    edit_device,
    remove_device,
)

router = APIRouter(prefix="/api/devices", tags=["Devices"])


class DeviceCreate(BaseModel):
    customer_id: int
    device_type: str = Field(min_length=1, max_length=80)
    brand: str = Field(min_length=1, max_length=100)
    model: str = Field(min_length=1, max_length=100)
    serial_no: str = Field(min_length=1, max_length=100)
    purchase_date: str | None = None
    warranty_end_date: str | None = None


@router.get("")
def lookup_device(serial_no: str | None = Query(None)):
    try:
        if serial_no is None:
            return get_devices()

        device = get_device_by_serial(serial_no)

        if device is None:
            raise HTTPException(
                status_code=404,
                detail="Device not found",
            )

        return device

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi truy vấn thiết bị",
        )


@router.post("", status_code=201)
def create_device_api(data: DeviceCreate):
    try:
        return add_device(
            data.customer_id,
            data.device_type,
            data.brand,
            data.model,
            data.serial_no,
            data.purchase_date,
            data.warranty_end_date,
        )

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Customer không tồn tại hoặc Serial/IMEI đã tồn tại",
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi tạo thiết bị",
        )


@router.get("/{device_id}")
def get_device_api(device_id: int):
    device = get_device(device_id)

    if device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return device


@router.put("/{device_id}")
def update_device_api(device_id: int, data: DeviceCreate):
    try:
        device = edit_device(
            device_id,
            data.customer_id,
            data.device_type,
            data.brand,
            data.model,
            data.serial_no,
            data.purchase_date,
            data.warranty_end_date,
        )

        if device is None:
            raise HTTPException(
                status_code=404,
                detail="Device not found",
            )

        return device

    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))
    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Customer không tồn tại hoặc Serial/IMEI đã tồn tại",
        )
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi cập nhật thiết bị",
        )


@router.delete("/{device_id}")
def delete_device_api(device_id: int):
    try:
        deleted = remove_device(device_id)

        if not deleted:
            raise HTTPException(
                status_code=404,
                detail="Device not found",
            )

        return {
            "message": "Device deleted successfully",
            "device_id": device_id,
        }

    except IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Không thể xóa thiết bị vì đang được liên kết với dữ liệu khác",
        )
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Lỗi xóa thiết bị",
        )