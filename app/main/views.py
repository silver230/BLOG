from flask import Flask
from . import main
from flask import render_template,redirect, request, url_for,abort,flash
from flask_login import login_required, current_user
from ..models import User,Blog,Comment
from .forms import BlogForm,UpdateProfile,CommentForm
from .. import db, photos


app = Flask(__name__)


# views
@main.route("/")
def index():
    
    title = 'Get started with a blog'
    blogs= Blog.query.all()

    return render_template('index.html', title= title,blogs=blogs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)        

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

        
    return redirect(url_for('main.profile',uname=uname))            


    
@main.route('/blog/new', methods=['GET', 'POST'])  
@login_required
def new_blog():
    form= BlogForm()

    if form.validate_on_submit():
        title = form.title.data 
        content = form.content.data 
        category = form.category.data 

        blog = Blog(title = title,content = content, category = category)

        db.session.add(blog)
        db.session.commit()

        print('blog')
        flash('Creating blog has been successful!')
        return redirect(url_for('main.one_blog', id = blog.id))


    return render_template('new_blog.html', title='New Blog',blog_form = form, legend = 'New Blog') 

@main.route('/blog/new/<int:id>')
def one_blog(id):
    blog = Blog.query.get(id)
    return render_template('blog.html', blog = blog)



@main.route('/blog/<int:blog_id>/',methods = ["GET","POST"])
def blog(blog_id):
    blog = Blog.query.filter_by(id=blog_id)
    form = CommentForm()

    if form.validate_on_submit():
     
        comment = form.comment.data 
        new_blog_comment = Comment(comment=comment,blog_id = blog_id)

        db.session.add(new_blog_comment) 
        db.session.commit()

    comments = Comment.query.filter_by(blog_id=blog_id)
    return render_template('comments.html', title = 'blog', blog =blog, blog_form = form, comments = comments) 






        
