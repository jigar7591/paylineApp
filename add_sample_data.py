from app import app
from models import db, Customer

with app.app_context():
    db.create_all()

    # Add sample customers
    if not Customer.query.first():
        sample_customers = [
            Customer(name='Jigar vaghela', card_number='1234567890', membership_number='ABC123', date_of_birth='1980-01-01', address='123 Main St'),
            Customer(name='Akash Patel', card_number='2345678901', membership_number='DEF456', date_of_birth='1990-02-02', address='456 Elm St'),
            Customer(name='Dinesh Mody', card_number='2349878901', membership_number='DEF456', date_of_birth='1990-05-02', address='456 Elm St')
        
        ]

        db.session.bulk_save_objects(sample_customers)
        db.session.commit()
