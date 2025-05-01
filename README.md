
# 중복 키워드 확인 API (Flask)

이 프로젝트는 기존에 작성한 키워드 목록을 기준으로, 
새로 작성할 키워드가 중복되는지를 확인할 수 있는 간단한 Flask API입니다.

## 실행 방법

### 1. 필요한 패키지 설치
```
pip install -r requirements.txt
```

### 2. 서버 실행
```
python app.py
```

### 3. API 사용 예시 (POST 요청)
- URL: http://localhost:5000/check_keywords
- JSON Body 예시:
```
{
  "keywords": "일산 점집, 연애운"
}
```
