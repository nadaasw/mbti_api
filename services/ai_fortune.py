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
    너는 신통방통한 점술가야. 사용자의 MBTI({mbti})에 따라 올해의 운세를 점쳐줘.
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