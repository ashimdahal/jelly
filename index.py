from flask import Flask, render_template, request, jsonify, make_response
import json
import os
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def api():
    # Fetching the cookie 
    cookie= request.cookies.get('cookieToken')
    if 'cookieToken' in request.cookies:
        return render_template('index.html')

    if request.method == 'POST':
        token = request.form.get('token')
        # with open(os.path.join('bot','token.txt'), 'w') as e:
        #     e.write(token)
        # seting the cookie
        expire_date= datetime.datetime.now() + datetime.timedelta(days=365)
        cookieToken = make_response(render_template('index.html'))
        cookieToken.set_cookie('cookieToken', f'{token}', expires=expire_date)
        return cookieToken       
    return render_template('api.html')


# Gets user's input, runs it through the talk function in conversation.py and generates the output
@app.route('/getresponse',methods=['POST'])
def response():
    from conversation import talk
    token = request.cookies.get('cookieToken')
    user_inp = request.get_json()
    text = user_inp['text']
    prev_conv = user_inp['previous_conversaion']
    out = talk(text,prev_conv,token)
    return jsonify(out)

@app.route('/removetoken')
def remove():
    resp = make_response(render_template('api.html'))
    resp.set_cookie('cookieToken', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
