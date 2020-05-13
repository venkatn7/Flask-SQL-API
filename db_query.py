from main import User
from flask import jsonify

x = User.query.all()
y = User.query.filter_by(username='ven_123').first()
z = User.query.get(31)
print(jsonify(z))

# def qrest():
#     with app.app_context():
#         users = User.query.all()
#         print(users)
