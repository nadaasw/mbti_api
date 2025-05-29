from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from services.ai_fortune import analyze_psychology_answers

router = APIRouter()

class AnswerItem(BaseModel):
    question: str
    answer: str

@router.post("/psychology/analyze")
def analyze_psychology(answers: List[AnswerItem]):
    return analyze_psychology_answers([a.dict() for a in answers])

# 항상 리락쿠마 결과 반환
@router.post("/psychology/fixed")
def fixed_psychology_result(answers: List[AnswerItem]):
    return {
        "character": "리락쿠마",
        "summary": "겉으로는 느긋하고 조용하지만, 속에는 따뜻한 감성과 자기만의 세계가 뚜렷한 사람이다. 규칙보다는 자유를, 경쟁보다는 평온함을 선호하며, 타인의 시선을 의식하기보다는 자신이 편한 리듬대로 살아간다. 말수가 적어도 주변을 세심하게 관찰하고, 사소한 것에서 행복을 잘 느끼며 감정 표현은 조용하지만 깊다. 누군가에게 쉽게 다가가지 않지만, 한번 마음을 열면 진심으로 연결되고자 한다. 리락쿠마처럼 소란한 세상 속에서도 자신만의 속도로 삶을 즐길 줄 아는 조용한 감성주의자다.",
        "mbtiGuess": "ISFP",
        "recommand_music": "실리카겔, 새소년"
    }