from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
# from models import db, User
from connectlink.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template
from flask_login import login_required, current_user
# updated libs for profile pic adjustment
import os
from werkzeug.utils import secure_filename
# Create a Blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return render_template('index.html')

@auth_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


# for profile picture start
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to update the profile picture
@auth_bp.route('/update-profile-picture', methods=['POST'])
@login_required
def update_profile_picture():
    if 'profile_image' not in request.files:
        flash('No file part', 'danger')
        return redirect(request.url)

    file = request.files['profile_image']

    if file and allowed_file(file.filename):
        filename = secure_filename(f"{current_user.id}_{file.filename}")  # Ensure a unique filename
        file_path = os.path.join(current_app.root_path, 'static/images/profiles', filename)
        
        file.save(file_path)  # Save the file to the 'profiles' folder

        # Update the user's profile image in the database
        current_user.profile_image = filename
        db.session.commit()

        flash('Profile picture updated successfully!', 'success')
    else:
        flash('Invalid file type. Please upload a PNG, JPG, or JPEG image.', 'danger')

# added auth to make it auth.dashboard --- error fixing
    return redirect(url_for('auth.dashboard'))
# dp
# Sign-up route
@auth_bp.route('/register', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

  # Hash the password before storing it
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        if username and email and password:
            # hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, email=email, password_hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Sign-up successful! You can now log in.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Please fill in all fields!', 'danger')
    return render_template('register.html')

# Login route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            login_user(user)
            flash('Logged in successfully!', 'success')
            # fixed the dashboard reachability 9.03am wednesday
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

# Logout route
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('auth.login'))

# Dashboard route
# Profile route