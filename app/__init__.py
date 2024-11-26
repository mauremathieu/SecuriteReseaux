from flask import Flask

def create_app(config_class):
    app = Flask(__name__)
    
    # Load the configuration
    app.config.from_object(config_class)
    
    # Import and register blueprints
    from .routes import main_bp
    
    app.register_blueprint(main_bp)
    
    return app