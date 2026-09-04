import os
from datetime import datetime
from flask import Flask
from dotenv import load_dotenv
from blueprints.home.routes import bp as home_bp
from blueprints.about.routes import bp as about_bp
from blueprints.products.routes import bp as products_bp
from blueprints.careers.routes import bp as careers_bp
from blueprints.contact.routes import bp as contact_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-change-me')

    app.register_blueprint(home_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(careers_bp)
    app.register_blueprint(contact_bp)

    @app.context_processor
    def inject_globals():
        return {'current_year': datetime.utcnow().year}

    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=False, port=5000)
