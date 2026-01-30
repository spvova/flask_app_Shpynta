from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length, Regexp


CATEGORIES = [
    ('news', 'News'),
    ('publication', 'Publication'),
    ('tech', 'Tech'),
    ('other', 'Other')
]


class ContactForm(FlaskForm):
    name = StringField(
        'Name',
        validators=[
            DataRequired(),
            Length(min=4, max=10, message="Ім'я повинно бути від 4 до 10 символів")
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message="Некоректна email адреса")
        ]
    )

    phone = StringField(
        'Phone',
        validators=[
            DataRequired(),
            Regexp(
                r'^\+380\d{9}$',
                message="Телефон має бути у форматі +380XXXXXXXXX"
            )
        ]
    )

    subject = SelectField(
        'Subject',
        choices=[
            ('support', 'Підтримка'),
            ('order', 'Замовлення'),
            ('other', 'Інше')
        ],
        validators=[DataRequired()]
    )

    message = TextAreaField(
        'Message',
        validators=[
            DataRequired(),
            Length(max=500, message="Повідомлення до 500 символів")
        ]
    )

    submit = SubmitField('Send')


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=2)])
    content = TextAreaField("Content", render_kw={"rows": 5, "cols": 40}, validators=[DataRequired()])
    is_active = BooleanField('Active Post')
    category = SelectField('Category', choices=CATEGORIES, validators=[DataRequired()])
    author_id = SelectField('Author', coerce=int, validators=[DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)

    submit = SubmitField("Add Post")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Завантажуємо авторів з БД під час ініціалізації форми
        from app.users.models import User
        from app.posts.models import Tag
        from app import db
        from sqlalchemy import select
        
        users = db.session.execute(select(User).order_by(User.id)).scalars().all()
        self.author_id.choices = [(u.id, u.username) for u in users]
        
        # Завантажуємо теги з БД
        tags = db.session.execute(select(Tag).order_by(Tag.name)).scalars().all()
        self.tags.choices = [(t.id, t.name) for t in tags]
