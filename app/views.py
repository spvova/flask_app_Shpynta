from flask import Blueprint, render_template, flash, redirect, url_for
from .form import ContactForm  # імпорт твоєї форми ContactForm

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def index():
    return render_template('base.html')

@views_bp.route('/contacts', methods=['GET', 'POST'])
def contacts():
    form = ContactForm()
    if form.validate_on_submit():
        # Тут можна обробити дані, наприклад, зберегти або надіслати email
        flash('Повідомлення надіслано успішно!', 'success')
        return redirect(url_for('views.contacts'))
    return render_template('contacts.html', form=form)

@views_bp.route('/resume')
def resume():
    return render_template('resume.html')
