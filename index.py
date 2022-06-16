from flask import Flask, render_template, request, jsonify
from conversation import *
import json

app = Flask(__name__)
app.config['FOLDER_NAME']=    'nlp'
app.config['SECRET_KEY'] = 'super_secret_key'


@app.route('/', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        file =request.files['file']
        token = request.form.get('token')
        with open('bot/token.txt', 'w') as e:
            e.write(token)
        file.save(os.path.join(app.config['FOLDER_NAME'],secure_filename(file.filename)))

        return redirect('/home')
        
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
