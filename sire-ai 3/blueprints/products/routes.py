from flask import Blueprint, render_template

bp = Blueprint('products', __name__, template_folder='../../templates/products')


@bp.route('/products')
def index():
    return render_template('products/index.html', active='products')
