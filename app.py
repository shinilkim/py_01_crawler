from flask import Flask
from flask import render_template
from flask import request,jsonify, abort, json

from classes.controller.naverController import NaverController

app = Flask(__name__)

# 01. index
@app.route('/', methods=['GET'])
def index():
    return render_template('/naver/index.html')

# 02. 네이버 뉴스 크롤러
@app.route('/crawler/naver')
def crawler_naver():
    controller = NaverController()
    return render_template('/naver/include/naver.html', data=controller.getNewsList())

@app.route('/crawler/daum/<name>')
def crawler_daum(name):
    return render_template("/daum/"+name+".html")

@app.route('/api/daum', methods=['GET','POST','DELETE'])
def api_daum():
    from classes.controller.daumController import DaumController
    controller = DaumController()
    print(request.get_json() or {})
    return jsonify(eval("controller."+request.args.get("method")+"()"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

