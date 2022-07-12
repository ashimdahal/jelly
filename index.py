from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import json
import os
import datetime

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://xahwfrorjlrcnn:f9da5fbcb2b3146ddef24e1f4263152beb4732f757c6743ead949237544e8c02@ec2-52-20-166-21.compute-1.amazonaws.com:5432/dctfl6qp4tki9e'

class Users(db.Model):
    sno = db.Column(db.Integer, nullable=True, primary_key=True)
    newUsers = db.Column(db.Integer, nullable=True)
    dailyUsers = db.Column(db.Integer, nullable=True)
    weeklyUsers = db.Column(db.Integer,  nullable=True)
    monthlyUsers = db.Column(db.Integer,  nullable=True)


@app.route('/', methods=['GET', 'POST'])
def api():

    if 'cookieToken' in request.cookies:
         # Fetching the cookie 
        cookie= request.cookies.get('cookieToken')
        # fetching data from database
        User =  Users.query.filter_by(sno=1).first()
        if 'dayCookie' in request.cookies:
            day=User.dailyUsers+1
            User.dailyUsers=day
            week=User.weeklyUsers+1
            User.weeklyUsers=week
            month=User.monthlyUsers+1
            User.monthlyUsers=month
            db.session.commit()
        elif 'weekCookie' in request.cookies:
            day=User.dailyUsers+1
            User.dailyUsers=day
            week=User.weeklyUsers+1
            User.weeklyUsers=week
            month=User.monthlyUsers+1
            User.monthlyUsers=month
            db.session.commit()
        elif 'monthCookie' in request.cookies:
            day=User.dailyUsers+1
            User.dailyUsers=day
            week=User.weeklyUsers+1
            User.weeklyUsers=week
            month=User.monthlyUsers+1
            User.monthlyUsers=month
            db.session.commit()
        else:
            # setting the cookie for new monthly user
            cookieToken = make_response(render_template('index.html'))
            cookieToken.set_cookie('dayCookie', f'{cookie}' , expires=datetime.datetime.now() + datetime.timedelta(days=1))
            cookieToken.set_cookie('weekCookie', f'{cookie}' , expires=datetime.datetime.now() + datetime.timedelta(days=7))
            cookieToken.set_cookie('monthCookie', f'{cookie}' , expires=datetime.datetime.now() + datetime.timedelta(days=30))
            new=User.newUsers+1
            User.newUsers=new
            day=User.dailyUsers+1
            User.dailyUsers=day
            week=User.weeklyUsers+1
            User.weeklyUsers=week
            month=User.monthlyUsers+1
            User.monthlyUsers=month
            db.session.commit()
            return cookieToken
        return render_template('index.html')

    if request.method == 'POST':
        # seting the cookie
        token = request.form.get('token')
        # main cookie
        expire_date= datetime.datetime.now() + datetime.timedelta(days=365)
        cookieToken = make_response(render_template('index.html'))
        cookieToken.set_cookie('cookieToken', f'{token}', expires=expire_date)

        User =  Users.query.filter_by(sno=1).first()
        cookieToken.set_cookie('dayCookie', f'{token}' , expires=datetime.datetime.now() + datetime.timedelta(days=1))
        cookieToken.set_cookie('weekCookie', f'{token}' , expires=datetime.datetime.now() + datetime.timedelta(days=7))
        cookieToken.set_cookie('monthCookie', f'{token}' , expires=datetime.datetime.now() + datetime.timedelta(days=30))
        new=User.newUsers+1
        User.newUsers=new
        day=User.dailyUsers+1
        User.dailyUsers=day
        week=User.weeklyUsers+1
        User.weeklyUsers=week
        month=User.monthlyUsers+1
        User.monthlyUsers=month
        db.session.commit()
        return cookieToken       
    return render_template('api.html')


# Gets user's input, runs it through the talk function in conversation.py and generates the output
@app.route('/getresponse',methods=['POST'])
def response():
    from conversation import talk
    token = request.cookies.get('cookieToken')
    pring(token)
    user_inp = request.get_json()
    text = user_inp['text']
    prev_conv = user_inp['previous_conversaion']
    out = talk(text,prev_conv,token)
    return jsonify(out)

@app.route('/removetoken')
def remove():
    resp = make_response(render_template('api.html'))
    resp.set_cookie('cookieToken', expires=0)
    resp.set_cookie('dayCookie', expires=0)
    resp.set_cookie('weekCookie', expires=0)
    resp.set_cookie('monthCookie', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
