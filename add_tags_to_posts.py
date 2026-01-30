from app import create_app, db
from app.posts.models import Post, Tag
from sqlalchemy import select

app = create_app()
with app.app_context():
    # Додаємо теги
    tags = [
        Tag(name='Django'),
        Tag(name='REST'),
        Tag(name='SQLAlchemy'),
        Tag(name='Web Development'),
    ]
    
    db.session.add_all(tags)
    db.session.commit()
    
    print('✓ Додано теги:')
    for tag in tags:
        print(f'  - {tag}')
    
    # Отримуємо існуючі пости та додаємо їм теги
    posts = db.session.execute(select(Post)).scalars().all()
    
    # Першому посту додаємо теги Python, Flask
    if len(posts) > 0:
        posts[0].tags.append(db.session.execute(select(Tag).where(Tag.name == 'Python')).scalar())
        posts[0].tags.append(db.session.execute(select(Tag).where(Tag.name == 'Flask')).scalar())
    
    # Другому посту додаємо теги Django, REST
    if len(posts) > 1:
        posts[1].tags.append(db.session.execute(select(Tag).where(Tag.name == 'Django')).scalar())
        posts[1].tags.append(db.session.execute(select(Tag).where(Tag.name == 'REST')).scalar())
    
    # Третьому посту додаємо теги SQLAlchemy, Web Development
    if len(posts) > 2:
        posts[2].tags.append(db.session.execute(select(Tag).where(Tag.name == 'SQLAlchemy')).scalar())
        posts[2].tags.append(db.session.execute(select(Tag).where(Tag.name == 'Web Development')).scalar())
    
    db.session.commit()
    
    print('\n=== ТЕГИ ДЛЯ КОЖНОГО ПОСТА ===')
    for post in posts:
        print(f'\nПост: "{post.title}"')
        if post.tags:
            for tag in post.tags:
                print(f'  - {tag.name}')
        else:
            print('  (Немає тегів)')
    
    print('\n=== ПОСТИ ДЛЯ КОЖНОГО ТЕГУ ===')
    all_tags = db.session.execute(select(Tag)).scalars().all()
    for tag in all_tags:
        print(f'\nТег: "{tag.name}"')
        if tag.posts:
            for post in tag.posts:
                print(f'  - {post.title}')
        else:
            print('  (Немає постів)')
