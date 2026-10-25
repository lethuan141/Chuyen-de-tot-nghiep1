
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.customer_routes import router as customer_router
from src.routes.device_routes import router as device_router
from src.routes.ticket_routes import router as ticket_router

app = FastAPI(
    title="Smart CRM - Mekong Mobile",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(customer_router)
app.include_router(device_router)
app.include_router(ticket_router)


@app.get("/")
def home():
    return {"message": "Smart CRM API is running"}
