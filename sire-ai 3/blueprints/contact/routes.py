from flask import Blueprint, render_template, request, redirect, url_for, flash

bp = Blueprint('contact', __name__, template_folder='../../templates/contact')


@bp.route('/contact', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        # In production: validate + send to CRM/email service.
        flash(f"Thanks{', ' + name if name else ''}. We'll get back to you within one business day.")
        return redirect(url_for('contact.index'))
    return render_template('contact/index.html', active='contact')
