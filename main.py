from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware
from routers import register, login

app = FastAPI(title="JWT Auth App with Rate Limiting")

# Подключаем SlowAPI middleware
app.state.limiter = register.limiter
app.add_exception_handler(register.limiter._rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(register.router)
app.include_router(login.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
