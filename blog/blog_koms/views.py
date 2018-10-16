# blog_koms/views.py

from flask import render_template,url_for,flash,request,redirect,Blueprint
from flask_login import current_user,login_required
from blog import db
from blog.models import BlogComment
from blog.blog_koms.forms import AddCommentForm

Views_Comms = Blueprint('Views_Comms',__name__)

####################################
### Tworzenie KOMENTARZA  ##########
####################################

@Views_Comms.route('/Create_Comm',methods=["GET",'POST'])
@login_required
def Create_Comms(post_id):

    BlogPost = Post.query.get_or_404(post_id)

    form = AddCommentForm()

    if form.validate_on_submit():

        Views_Comms = BlogComment(body=form.body.data,
                            	user_id=current_user.id,
                                article=post.id)
        db.session.add(Views_Comms)
        db.session.commit()
        flash("Twój komentarz zostanie dodany!", "success")
        return redirect(url_for('core.index', post_id=post.id))

    return render_template('Create_Comms.html',form=form)
