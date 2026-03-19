from fastapi import APIRouter, Depends, HTTPException, Header
from ..core.security import check_init_data

router = APIRouter()

@router.post("/validate")
async def validate_user(init_data: str = Header(...)):
    if not check_init_data(init_data):
        raise HTTPException(403, "Invalid initData")
    # Здесь можно вернуть user_id из init_data
    return {"valid": True}
