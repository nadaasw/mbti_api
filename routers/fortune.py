from fastapi import APIRouter, Query
from services.ai_fortune import (
    get_today_fortune_by_mbti,
    get_today_fortune_by_birthday,
    get_yearly_fortune_by_mbti,
    get_yearly_fortune_by_birthday
)

router = APIRouter(
    prefix="/fortune",
    tags=["fortune"]
)

### 🔮 "오늘의 운세" API ###
@router.get("/today/mbti")
async def get_today_mbti_fortune(mbti: str = Query(..., description="MBTI 입력")):
    """MBTI 기반 오늘의 운세"""
    fortune = get_today_fortune_by_mbti(mbti)
    return {"mbti": mbti, "fortune": fortune}

@router.get("/today/birthday")
async def get_today_birthday_fortune(birthday: str = Query(..., description="생년월일 입력")):
    """생년월일 기반 오늘의 운세"""
    fortune = get_today_fortune_by_birthday(birthday)
    return {"birthday": birthday, "fortune": fortune}

### 📅 "올해의 운세" API ###
@router.get("/year/mbti")
async def get_yearly_mbti_fortune(mbti: str = Query(..., description="MBTI 입력")):
    """MBTI 기반 올해의 운세"""
    fortune = get_yearly_fortune_by_mbti(mbti)
    return {"mbti": mbti, "fortune": fortune}

@router.get("/year/birthday")
async def get_yearly_birthday_fortune(birthday: str = Query(..., description="생년월일 입력")):
    """생년월일 기반 올해의 운세"""
    fortune = get_yearly_fortune_by_birthday(birthday)
    return {"birthday": birthday, "fortune": fortune}