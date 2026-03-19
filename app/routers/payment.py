from fastapi import APIRouter, Request
from yookassa import Configuration, Payment
from ..core.config import settings

Configuration.account_id = settings.yookassa_shop_id
Configuration.secret_key = settings.yookassa_secret_key

router = APIRouter()

@router.post("/create-subscription")
async def create_subscription(request: Request):
    data = await request.json()
    amount = 150  # + 50 * кол-во специалистов — считай здесь
    payment = Payment.create({
        "amount": {"value": f"{amount}.00", "currency": "RUB"},
        "confirmation": {
            "type": "redirect",
            "return_url": f"{settings.webapp_url}?success=1"
        },
        "capture": True,
        "save_payment_method": True,
        "description": "Подписка MarketService",
        "metadata": {"telegram_id": data.get("telegram_id")}
    })
    return {"confirmation_url": payment.confirmation.confirmation_url}
