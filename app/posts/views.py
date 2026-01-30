from flask import render_template, abort, request, redirect, url_for, flash
from . import post_bp
from app import db
from app.posts.models import Post
from app.form import PostForm


@post_bp.route('/posts')
def index():
    page = request.args.get('page', 1, type=int)
    posts = db.session.query(Post).paginate(page=page, per_page=10)
    return render_template('posts/posts.html', posts=posts.items, pagination=posts)


@post_bp.route('/posts/<int:post_id>')
def detail(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        abort(404)
    return render_template('posts/detail_post.html', post=post)


@post_bp.route('/posts/add', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        # Створюємо новий пост
        post = Post(
            title=form.title.data,
            content=form.content.data,
            category=form.category.data,
            user_id=form.author_id.data
        )
        # Додаємо теги
        from app.posts.models import Tag
        if form.tags.data:
            tags = db.session.query(Tag).filter(Tag.id.in_(form.tags.data)).all()
            post.tags = tags
        
        db.session.add(post)
        db.session.commit()
        flash(f'Post "{post.title}" created successfully!', 'success')
        return redirect(url_for('posts.detail', post_id=post.id))
    
    return render_template('posts/add_post.html', form=form)
