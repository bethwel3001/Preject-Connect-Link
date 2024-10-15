from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from connectlink.routes import auth_bp
# Initialize Flask app

# connecting to models.py in the connectlink folder
from connectlink.models import db, User, Service
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/connectlink'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'supersecretkey'  # Update to a secure key for production

# Initialize SQLAlchemy and Flask-Migrate
db.init_app(app)

# Register the authentication blueprint
app.register_blueprint(auth_bp)
# Initialize Flask-Migrate
migrate = Migrate(app, db)  # Handles database migrations

# Create tables (only if they don't exist already)
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    # homepage
    return render_template('index.html', message="Welcome to Connect-Link!") 

@app.route('/users')
def list_users():
    """Display all users registered in the system."""
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    """Add a new user to the database."""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')  # In production, hash the password
        if username and email and password:
            new_user = User(username=username, email=email, password_hash=password)
            db.session.add(new_user)
            db.session.commit()
            flash('User added successfully!', 'success')
            return redirect(url_for('list_users'))
        else:
            flash('Please fill all fields!', 'danger')
    return render_template('add_user.html')

# Error handling route for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
