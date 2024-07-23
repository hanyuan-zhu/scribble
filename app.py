from flask import Flask, render_template, request, jsonify
from dashscope import Application
from http import HTTPStatus
import markdown


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']

    # 调用AI API
    response = Application.call(
        app_id='9ec0a032b64c4a8ca3a53812148f2c64',
        prompt=user_input,
        api_key='sk-543852492eb747f7b8fd4a4904409ae7',
    )

    if response.status_code != HTTPStatus.OK:
        return jsonify({"error": f'request_id={response.request_id}, code={response.status_code}, message={response.message}'})
    else:
        ai_output = response.output.text
        # 将Markdown文本转换为HTML
        ai_output_html = markdown.markdown(ai_output)
        return jsonify({"content": ai_output_html})

if __name__ == '__main__':
    app.run(debug=True)
