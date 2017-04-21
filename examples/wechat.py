'''
    wechat
    --------
    A simple Flask demo app that shows how to login with WeChat via rauth.
    Please note: you must do `from wechat import db; db.create_all()` from
    the interpreter before running this example!

    Due to WeChat's stringent domain validation, requests using this app
    must originate from 127.0.0.1:5000.
'''

from flask import Flask, flash, request, redirect, render_template, url_for

from wechat_oauth2 import WeChatService


# Flask config
SECRET_KEY = '\xfb\x12\xdf\xa1@i\xd6>V\xc0\xbb\x8fp\x16#Z\x0b\x81\xeb\x16'
DEBUG = True
WX_APPID = 'your appid'
WX_SECRET = 'your app secret'

# Flask setup
app = Flask(__name__)
app.config.from_object(__name__)

# WeChat OAuth 2.0 service wrapper
wechat = WeChatService(app.config['WX_APPID'],
                       app.config['WX_SECRET'])


# views
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/wechat/login')
def login():
    redirect_uri = url_for('authorized', _external=True)
    params = {'redirect_uri': redirect_uri, 'scope': 'snsapi_userinfo'}
    return redirect(wechat.get_authorize_url(**params))


@app.route('/wechat/authorized')
def authorized():
    # check to make sure the user authorized the request
    if 'code' not in request.args:
        flash('You did not authorize the request')
        return redirect(url_for('index'))

    # make a request for the access token credentials using code
    session = wechat.get_auth_session(request.args['code'])

    # the "me" response
    me = session.get('userinfo').json()

    flash('Logged in as ' + me['nickname'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    # db.create_all()
    app.run(host='0.0.0.0')
