from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates  # если захочешь шаблоны
from pathlib import Path
import hmac
import hashlib
import time
from urllib.parse import parse_qs
from .routers import auth, company, payment
from .core.config import settings

app = FastAPI(title="MarketService Mini App")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth.router, prefix="/api/auth")
app.include_router(company.router, prefix="/api/company")
app.include_router(payment.router, prefix="/api/payment")

@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = Path("app/static/index.html")
    if not index_path.exists():
        return "<h1>index.html не найден</h1>"
    return index_path.read_text()

@app.get("/success")
async def payment_success(request: Request):
    # Здесь можно показать страницу успеха
    return RedirectResponse("/static/index.html?success=1")

# Проверка initData (очень упрощённо — в продакшене используй полную проверку)
def check_init_data(init_data: str) -> bool:
    try:
        parsed = parse_qs(init_data)
        hash_str = parsed.pop("hash")[0]
        data_check_string = "\n".join(f"{k}={v[0]}" for k, v in sorted(parsed.items()))
        secret_key = hashlib.sha256(settings.secret_key.encode()).digest()
        calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
        return calculated_hash == hash_str
    except:
        return False

print("Запуск: http://localhost:8000/static/index.html")
