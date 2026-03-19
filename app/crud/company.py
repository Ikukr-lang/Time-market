from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..core.database import SessionLocal
from ..models.company import Company

router = APIRouter()

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.get("/my")
async def get_my_company(telegram_id: int, db: AsyncSession = Depends(get_db)):
    # упрощённо — в реальности ищи по telegram_id
    return {"name": "Test Company", "trial_days_left": 5}
