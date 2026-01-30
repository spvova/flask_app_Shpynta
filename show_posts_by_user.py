from app import create_app, db
from app.posts.models import Post
from app.users.models import User
from sqlalchemy import select

app = create_app()
with app.app_context():
    # Користувач з id=2
    user2 = db.session.execute(select(User).where(User.id == 2)).scalar()
    print(f"=== Пости користувача {user2.username} (id=2) ===")
    posts_user2 = db.session.execute(select(Post).where(Post.user_id == 2)).scalars().all()
    for post in posts_user2:
        print(f"  {post.id}. {post.title} - {post.category}")
    
    # Користувач з id=1
    user1 = db.session.execute(select(User).where(User.id == 1)).scalar()
    print(f"\n=== Пости користувача {user1.username} (id=1) ===")
    posts_user1 = db.session.execute(select(Post).where(Post.user_id == 1)).scalars().all()
    if posts_user1:
        for post in posts_user1:
            print(f"  {post.id}. {post.title} - {post.category}")
    else:
        print("  Постів немає")
