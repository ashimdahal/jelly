from flask import Flask, render_template, request, jsonify
from conversation import *
import json
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def api():
    if os.path.exists(os.path.join('bot','token.txt')):
        return render_template('index.html')

    if request.method == 'POST':
        token = request.form.get('token')
        with open(os.path.join('bot','token.txt'), 'w') as e:
            e.write(token)
        return render_template('index.html')
        
    return render_template('api.html')


# Gets user's input, runs it through the talk function in conversation.py and generates the output
@app.route('/getresponse',methods=['POST'])
def response():
    user_inp = request.get_json()
    text = user_inp['text']
    prev_conv = user_inp['previous_conversaion']
    out = talk(text,prev_conv)
    return jsonify(out)

if __name__ == '__main__':
    app.run(debug=True)
