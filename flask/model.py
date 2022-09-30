from flask import render_template, request,Blueprint
from flask import redirect, url_for, session, abort, flash

import base64 as bs64

import fooBase as fb
import blog


md = Blueprint('model',__name__,template_folder='foo')

@md.route('/', methods=['GET', 'POST'])
def index():
    blog_get = [x  for x in fb.dbb.session.query(fb.Blog).distinct()]
    if request.method == 'POST':
        if 'login' in request.form:
            return redirect(url_for('model.login'))
        if 'regist' in request.form:
            return redirect(url_for('model.regist'))
    return render_template('home.html', name='User',blogs=blog_get)


@md.route('/profile/<string:user>', methods=['GET','POST'])
def profile(user):
  blog_get = [x  for x in fb.dbb.session.query(fb.Blog).filter(fb.Blog.username == user).distinct()]
  if 'userLogin' not in session or session['userLogin'] != user:
    abort(401)

  if request.method == 'POST':
    if 'login_out' in request.form:
      session.pop('userLogin', None)
      return redirect(url_for('model.index'))
    if 'blog'in request.form:
      return redirect(url_for('blog.blog'))
    if 'indexpage' in request.form:
      return redirect(url_for('model.index'))
  return render_template('profile.html', users=user,blogs=blog_get)

@md.route("/login", methods=['GET', 'POST'])
def login():
  user_name = [x.username for x in fb.dbb.session.query(fb.User.username).distinct()]
  psw = [x.password for x in fb.dbb.session.query(fb.User.password).distinct()]
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    
    psw64 = str(bs64.b64encode(password.encode("UTF-8")))[2:-1]

    if username in user_name and psw64 in str(psw):
      session['userLogin'] = username
      return redirect(url_for('model.profile', user=session['userLogin']))
    else:
      flash('Неверный пароль или имя пользователя')
    
  return render_template('login.html')

@md.route('/regist',methods=['GET','POST'])
def regist():
  if request.method == 'POST':
    user_name = [x.username for x in fb.dbb.session.query(fb.User.username).distinct()]
    emails = [x.email for x in fb.dbb.session.query(fb.User.email).distinct()]
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    psw64 = bs64.b64encode(password.encode("UTF-8"))
    if email not in emails and username not in user_name:
      user = fb.User(username=username,email=email,password=psw64)
      fb.dbb.session.add(user)
      fb.dbb.session.flush()
      fb.dbb.session.commit()
      session['userLogin'] = username
      return redirect(url_for('model.profile',user=username))
    else:
      flash('Такой пользователь или почта уже существуют')

  return render_template('registr.html')
  