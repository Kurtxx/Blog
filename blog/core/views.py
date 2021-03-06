# core/views.py

from flask import render_template,request,Blueprint
from blog.models import BlogPost, BlogComment

core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    Views_Comms = BlogComment.query.order_by(BlogComment.date.desc())
    return render_template('index.html',blog_posts=blog_posts,Views_Comms=Views_Comms)

@core.route('/info')
def info():
    return render_template('info.html')
