
from flask import Flask, request, jsonify
from collections import Counter

app = Flask(__name__)

# 기존 키워드 (이 리스트는 필요 시 파일로 불러오거나 DB 연동 가능)
existing_keywords = [
    "일산 점집", "일산 점집", "서울점집", "서울점집", "안산점집",
    "용한점집", "유명한 점집", "안산 점집"
]

keyword_counter = Counter(existing_keywords)

@app.route("/check_keywords", methods=["POST"])
def check_keywords():
    input_data = request.json
    input_keywords = input_data.get("keywords", "")
    keywords_to_check = [kw.strip() for kw in input_keywords.split(",")]
    result = {}

    for kw in keywords_to_check:
        count = keyword_counter.get(kw, 0)
        result[kw] = "✅ 중복" if count > 0 else "🆗 사용 가능"

    return jsonify(result)

@app.route("/", methods=["GET"])
def home():
    return "<h2>중복 키워드 확인 API</h2><p>POST /check_keywords with JSON {'keywords': '키워드1, 키워드2'}</p>"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




