import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드
api_key = os.getenv("OPENAI_API_KEY")

print(f"API Key: {api_key}")  # 환경 변수가 올바르게 불러와지는지 확인