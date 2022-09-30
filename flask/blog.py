from flask import render_template, request
from flask import redirect, url_for, session, abort, Blueprint

from __init__ import app
import fooBase as fb 
import model

bl = Blueprint('blog',__name__,template_folder='foo')

@bl.route('/blog', methods=['GET', 'POST'])
def blog():
  if 'userLogin' not in session or session['userLogin'] != session['userLogin']:
    abort(401)

  if request.method == 'POST':
    blogss = request.form.get('blog')
    blogUser = fb.Blog(username=session['userLogin'],blogs=blogss)
    fb.dbb.session.add(blogUser)
    fb.dbb.session.flush()
    fb.dbb.session.commit()
    return redirect(url_for('model.profile',user=session['userLogin']), code=302)
  
  return render_template('blog.html',username=session['userLogin'])