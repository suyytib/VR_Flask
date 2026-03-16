from flask import Blueprint, request
from flask import render_template
from zhipuai import ZhipuAI
def chat_with_gpt(messages): 
        client = ZhipuAI(api_key="8353581387f35d407501159e16135dd9.4WKkOMeSVa6kLRip") # 请填写您自己的APIKey
        response = client.chat.completions.create(
            model="glm-4-0520",
            messages=messages,
            top_p= 0.7,
            temperature= 0.9,
            max_tokens=4095,
            stream=True,
        )
        res=""
        for trunk in response:
            res+=trunk.choices[0].delta.content
        return res

bp=Blueprint("root",__name__,url_prefix="/root")
@bp.route('/')
def root():
    return render_template('root.html')

@bp.route('/yidu')
def yidu():
    return render_template('yidu.html')

@bp.route('/erdu')
def erdu():
    return render_template('erdu.html')

@bp.route('/sandu')
def sandu():
    return render_template('sandu.html')

@bp.route('/sidu')
def sidu():
    return render_template('sidu.html')

@bp.route('/yiyi')
def yiyi():
    return render_template('yiyi.html')

@bp.route('/chart/',methods=["POST"]) 
def chart():
    answer = request.form.get("answer")
    messages =[]
    user_input = answer
    messages.append({"role": "user", "content": user_input})
    response = chat_with_gpt(messages)
    print(response)
    return {
        'success': True,
        'message': response,
    }
