from flask import Blueprint, render_template

bp = Blueprint('careers', __name__, template_folder='../../templates/careers')

OPEN_ROLES = [
    {"title": "Research Engineer, ML Core", "team": "Research", "location": "Cambridge, MA", "type": "Full-time"},
    {"title": "Applied Scientist, Rise", "team": "Brokerage", "location": "Cambridge, MA", "type": "Full-time"},
    {"title": "Software Engineer, Inference Platform", "team": "Platform", "location": "Austin, TX", "type": "Full-time"},
    {"title": "Solutions Engineer, Enterprise", "team": "Enterprise", "location": "Austin, TX", "type": "Full-time"},
    {"title": "Product Designer", "team": "Product", "location": "Berlin, DE", "type": "Full-time"},
    {"title": "Developer Relations Lead", "team": "DevRel", "location": "Remote (US/EU)", "type": "Full-time"},
    {"title": "Security Engineer, Payments", "team": "Security", "location": "Cambridge, MA", "type": "Full-time"},
]


@bp.route('/careers')
def index():
    return render_template('careers/index.html', active='careers', roles=OPEN_ROLES)
