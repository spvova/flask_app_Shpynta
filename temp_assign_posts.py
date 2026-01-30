from app import create_app, db
from app.posts.models import Post
from app.users.models import User
from sqlalchemy import select

app = create_app()
with app.app_context():
    # Додаємо кілька постів без автора спочатку
    post1 = Post(title='First Post', content='Content 1', category='news')
    post2 = Post(title='Second Post', content='Content 2', category='publication')
    post3 = Post(title='Third Post', content='Content 3', category='tech')
    
    db.session.add_all([post1, post2, post3])
    db.session.commit()
    
    print('✓ Додано 3 поста без авторів')
    
    # Отримуємо користувача з id=2 (jane_smith)
    user2 = db.session.execute(select(User).where(User.id == 2)).scalar()
    
    # Отримуємо ці 3 поста та присвоюємо їм автора
    posts = db.session.execute(select(Post).where(Post.user_id == None)).scalars().all()
    
    for post in posts:
        post.user_id = user2.id
    
    db.session.commit()
    
    print(f'\n✓ Присвоєно користувача jane_smith (id=2) для {len(posts)} постів:')
    for post in posts:
        print(f'  - Post id={post.id}: "{post.title}" → {post.user.username}')
    
    print('\n=== ВСІ ПОСТИ ===')
    all_posts = db.session.execute(select(Post)).scalars().all()
    for post in all_posts:
        author = post.user.username if post.user else 'Без автора'
        print(f'  {post.id}. "{post.title}" → {author}')
