from flask import Blueprint, render_template

bp = Blueprint('about', __name__, template_folder='../../templates/about')


@bp.route('/about')
def index():
    return render_template('about/index.html', active='about')
