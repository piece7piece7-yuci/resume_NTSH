from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 中韓、中日翻譯共用路由
@app.route('/ask', methods=['GET', 'POST'])
def ask():

    if request.method == 'POST':

        # 讀取學生輸入的問題
        question = request.form.get('question', '').strip()

        # 讀取選擇的語言
        language = request.form.get('language', 'ko')

        # 根據語言選擇題庫
        if language == 'ko':
            dictionary = zh_ko_dict
            language_name = "韓文"
            template_name = "ask.html"

        elif language == 'jp':
            dictionary = zh_jp_dict
            language_name = "日文"
            template_name = "ask.html"

        # 查詢答案
        answer = dictionary.get(
            question,
            f"抱歉，我目前沒有這個詞的{language_name}對應。"
        )

        # 回傳答案
        return render_template(
            template_name,
            question=question,
            answer=answer,
            language=language
        )

    # GET 時給空白欄位
    return render_template(
        'ask.html',
        question="",
        answer="",
        language="ko"
    )
    
#改成互動 4/14
@app.route('/stock', methods=['GET', 'POST'])
def stock():
    if request.method == 'POST':
        # 2. 讀取股票號碼
        question = request.form.get('question', '').strip()
        # 3. 查詢股票號碼的對應股價

        answer = data["data"][-1][6]
   
    
    # API URL
    url = f"https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo={stock_no}"
    
    # 發送請求
    res = requests.get(url)
    data = res.json()
    
    # 判斷是否成功
    if data["stat"] == "OK":
        answer = data["data"][0][6]
        #print("收盤價：",data["data"][0][6])
    else:
        answer = "查無資料，請確認股票代號或日期"

        # 4. 回傳答案給使用者
        return render_template('stock.html', question=question, answer=answer)
    # GET 時給空白欄位
    return render_template('stock.html', question="", answer="")


@app.route('/leadership')
def leadership():
    return render_template('leadership.html')

@app.route('/club')
def club():
    return render_template('club.html')

@app.route('/electives')
def electives():
    return render_template('electives.html')

@app.route('/ai')
def ai():
    return render_template('ai.html')

@app.route('/Certificate')
def Certificate():
    return render_template('Certificate.html')


if __name__ == '__main__':
    app.run(debug=True)
