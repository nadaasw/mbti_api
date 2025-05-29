import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")  # .env 파일에서 API 키 불러오기
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # OpenAI API 키 설정

if api_key is None:
    print("❌ API 키가 로드되지 않았습니다. .env 파일이 존재하는지 확인하세요.")
else:
    print(f"✅ API Key Loaded: {api_key}")

# MBTI 별칭 설정
MBTI_ALIASES = {
    "ISTP": "만능재주꾼",
    "ISTJ": "청렴결백한 논리주의자",
    "ISFP": "호기심 많은 예술가",
    "ISFJ": "용감한 수호자",
    "INTP": "논리적인 사색가",
    "INTJ": "용의주도한 전략가",
    "INFP": "열정적인 중재자",
    "INFJ": "통찰력 있는 조언가",
    "ESTP": "모험을 즐기는 사업가",
    "ESTJ": "엄격한 관리자",
    "ESFP": "자유로운 영혼의 연예인",
    "ESFJ": "사교적인 외교관",
    "ENTP": "뜨거운 논쟁을 즐기는 변론가",
    "ENTJ": "대담한 통솔자",
    "ENFP": "재기발랄한 활동가",
    "ENFJ": "정의로운 사회운동가",
}

def get_today_fortune_by_mbti(mbti: str) -> str:
    """MBTI 기반 오늘의 운세"""
    mbti = mbti.upper()
    alias = MBTI_ALIASES.get(mbti, mbti)

    prompt = f"""
    너는 신통방통한 점술가야. 사용자의 MBTI({mbti})에 따라 오늘의 운세를 점쳐줘.
    하지만 {mbti} 대신 "{alias}"라는 별칭을 사용해서 운세를 알려줘.
    예를 들어, "오늘의 당신, {alias}님의 운세는 이렇습니다."와 같은 형식으로 응답해.
    """

    return get_fortune_from_openai(prompt)

def get_today_fortune_by_birthday(birthday: str) -> str:
    """생년월일 기반 오늘의 운세"""
    prompt = """
    너는 신통방통한 점술가야. 사용자의 생년월일을 기반으로 오늘의 운세를 점쳐줘.
    하지만 생년월일을 직접 언급하지 말고, "오늘의 당신,"이라고만 시작해서 운세를 알려줘.
    점성술, 띠별 운세, 사주 등의 개념을 활용하여 운세를 알려줘.
    """

    return get_fortune_from_openai(prompt)

def get_yearly_fortune_by_mbti(mbti: str) -> str:
    """MBTI 기반 올해의 운세"""
    mbti = mbti.upper()
    alias = MBTI_ALIASES.get(mbti, mbti)

    prompt = f"""
    너는 요즘 핫한 MBTI의 특성을 잘 아는 점술가야. 사용자의 MBTI({mbti})에 따라 올해의 운세를 점쳐줘.
    하지만 {mbti} 대신 "{alias}"라는 별칭을 사용해서 운세를 알려줘.
    예를 들어, "올해의 당신, {alias}님의 운세는 이렇습니다."와 같은 형식으로 응답해.
    """

    return get_fortune_from_openai(prompt)

def get_yearly_fortune_by_birthday(birthday: str) -> str:
    """생년월일 기반 올해의 운세"""
    prompt = """
    너는 신통방통한 점술가야. 사용자의 생년월일을 기반으로 올해의 운세를 점쳐줘.
    하지만 생년월일을 직접 언급하지 말고, "올해의 당신,"이라고만 시작해서 운세를 알려줘.
    점성술, 띠별 운세, 사주 등의 개념을 활용하여 운세를 알려줘.
    """

    return get_fortune_from_openai(prompt)

def get_fortune_from_openai(prompt: str) -> str:
    """OpenAI API를 이용해 운세를 가져옴"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

def analyze_psychology_answers(answers: list[dict]) -> dict:
    """사용자의 질문/답변 세트를 기반으로 성격을 분석하고 어울리는 캐릭터를 추천"""
    combined = "\n".join([f"Q: {item['question']}\nA: {item['answer']}" for item in answers])

    prompt = f"""
    너는 사람의 성격을 잘 분석하는 AI야.
    아래는 한 사용자가 심리 테스트에서 선택한 질문과 답변들이야:

    {combined}

    ---

    이제 위의 응답을 바탕으로, 다음 중 하나의 캐릭터를 **하나만** 골라 추천해줘.  
    추천 기준은 성격, 분위기, 에너지, 반응 스타일, 인간관계 등 전반적인 일치도를 고려해야 해.  
    캐릭터 이름과 한 줄 설명, 그리고 간단한 이유(2~3문장)를 함께 알려줘.  
    반드시 다음 중 하나여야 해:

    리락쿠마, 토토로, 하울, 키키, 소피, 짱구, 유미, 슬픔(감정이들), 렌고쿠, 카오나시, 엘사, 라푼젤, 주디 홉스, 미키마우스, 펭수, 무지, 피카츄, 잠만보, 시우(쿵푸팬더), 나루토

    출력 예시:

    ---
    👤 당신과 가장 어울리는 캐릭터는 **리락쿠마**입니다!  
    🪷 "무기력한 듯 여유로운 당신, 사실 누구보다 주변을 따뜻하게 품어주는 사람이에요."  
    항상 조용하고 편안한 분위기를 만들며, 누구에게도 부담 없이 다가오는 리락쿠마는 당신의 성향과 닮았습니다.
    아래 정보를 JSON 형식으로 응답해줘:

    {{
      "character": "추천 캐릭터 이름",
      "summary": "이 캐릭터와 닮은 이유를 설명하는 한 4줄 요약",
      "mbtiGuess": "예상되는 MBTI (선택 사항)"
    }}
    
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )

    try:
        return eval(response.choices[0].message.content)  # JSON 문자열을 딕셔너리로
    except Exception as e:
        return {"error": f"파싱 실패: {str(e)}"}