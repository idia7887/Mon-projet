    from fastapi import FastAPI
from app.api.V1.user import router

app = FastAPI()

@app.get("/")
def red_root():
    return{"statutus" : "ok"}

app.include_router(router)