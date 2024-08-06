from flask import Flask, render_template, redirect, url_for, request, flash
from models import db, User, Customer
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ensure the database is created before the first request
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Invalid email or password.', 'danger')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        card_number = request.form['card_number']
        membership_number = request.form['membership_number']
        date_of_birth = request.form['date_of_birth']
        address = request.form['address']
        
        # Check if the user already exists
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists.', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        
        new_user = User(email=email, password=hashed_password)
        db.session.add(new_user)
        
        new_customer = Customer(name=name, card_number=card_number, 
                                membership_number=membership_number, 
                                date_of_birth=date_of_birth, address=address)
        db.session.add(new_customer)
        
        db.session.commit()
        
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/search_customer', methods=['GET'])
def search_customer():
    search_term = request.args.get('search')
    if search_term:
        customers = Customer.query.filter(
            (Customer.name.ilike(f'%{search_term}%')) |
            (Customer.card_number.ilike(f'%{search_term}%')) |
            (Customer.membership_number.ilike(f'%{search_term}%')) |
            (Customer.date_of_birth.ilike(f'%{search_term}%')) |
            (Customer.address.ilike(f'%{search_term}%'))
        ).all()
    else:
        customers = []
    
    return render_template('welcome.html', customers=customers)
# Endpoint to handle payment with card
@app.route('/payment_with_card', methods=['POST'])
def payment_with_card():
    customer_name = request.form.get('customer_name')
    # Perform payment with card logic here
    flash(f'Processing payment with card for {customer_name}', 'info')
    return redirect(url_for('welcome'))
if __name__ == '__main__':
    app.run(debug=True)
