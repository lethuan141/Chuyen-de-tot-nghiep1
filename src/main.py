
from fastapi import FastAPI

from src.routes.customer_routes import router as customer_router
from src.routes.device_routes import router as device_router
from src.routes.ticket_routes import router as ticket_router

app = FastAPI(
    title="Smart CRM - Mekong Mobile",
    version="1.0.0",
)

app.include_router(customer_router)
app.include_router(device_router)
app.include_router(ticket_router)


@app.get("/")
def home():
    return {"message": "Smart CRM API is running"}
