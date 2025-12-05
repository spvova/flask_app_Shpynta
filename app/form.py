from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp

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
