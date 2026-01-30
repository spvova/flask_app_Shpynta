from datetime import datetime
from sqlalchemy import Integer, String, Text, DateTime, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app import db


# Асоціативна таблиця для зв'язку "багато до багатьох"
post_tags = db.Table(
    'post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)


class Post(db.Model):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    posted: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    
    # Enum для категорії
    category: Mapped[str] = mapped_column(
        Enum('news', 'publication', 'tech', 'other', name='post_category'),
        nullable=False,
        default='other'
    )
    
    # Foreign key до User
    user_id: Mapped[int | None] = mapped_column(ForeignKey('users.id'), nullable=True)
    # Двосторонній зв'язок з User
    user: Mapped["User | None"] = relationship("User", back_populates="posts")
    
    # Зв'язок "багато до багатьох" з тегами
    tags: Mapped[list["Tag"]] = relationship("Tag", secondary=post_tags, back_populates="posts")

    def __repr__(self):
        return f"<Post id={self.id}, title='{self.title}', category='{self.category}', user_id={self.user_id}>"


class Tag(db.Model):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    # Зв'язок "багато до багатьох" з постами
    posts: Mapped[list["Post"]] = relationship("Post", secondary=post_tags, back_populates="tags")

    def __repr__(self):
        return f"<Tag id={self.id}, name='{self.name}'>"