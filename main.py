from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import fortune

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lucky-mbti.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fortune.router)

@app.get("/")
async def root():
    return {"message": "운세 API 서버가 정상 작동 중입니다!"}