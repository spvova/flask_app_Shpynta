from app import create_app, db
from app.posts.models import Post, Tag
from sqlalchemy import select

app = create_app()
with app.app_context():
    # Додаємо тег
    tag1 = Tag(name='Python')
    tag2 = Tag(name='Flask')
    tag3 = Tag(name='Database')
    
    db.session.add_all([tag1, tag2, tag3])
    db.session.commit()
    
    # Отримуємо перший пост та додаємо йому теги
    post1 = db.session.execute(select(Post).limit(1)).scalar()
    post1.tags.append(tag1)
    post1.tags.append(tag2)
    
    db.session.commit()
    
    print(f"✓ Додано теги:")
    print(f"  - {tag1}")
    print(f"  - {tag2}")
    print(f"  - {tag3}")
    
    print(f"\n✓ Пост '{post1.title}' має теги:")
    for tag in post1.tags:
        print(f"  - {tag.name}")
    
    print(f"\n✓ Тег '{tag1.name}' присутній в постах:")
    for post in tag1.posts:
        print(f"  - {post.title}")
