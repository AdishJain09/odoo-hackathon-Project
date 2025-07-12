from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.question import question_bp
from routes.admin import admin_bp

app = Flask(__name__)
CORS(app)
app.config['JWT_SECRET_KEY'] = 'your_secret'
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(question_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(debug=True)
