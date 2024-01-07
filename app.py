

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'Hello, this is the home page!'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Use an application context to create tables
with app.app_context():
    # Create tables
    db.create_all()

# Routes for CRUD operations

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    new_item = Item(name=data['name'], description=data['description'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Item created successfully'}), 201

@app.route('/items', methods=['GET'])
def get_all_items():
    items = Item.query.all()
    items_list = [{'id': item.id, 'name': item.name, 'description': item.description} for item in items]
    return jsonify(items_list)

# ... (other routes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
