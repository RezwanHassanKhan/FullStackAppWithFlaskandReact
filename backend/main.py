from config import app , db
from models import Contact
from flask import request , jsonify

#implementing CRUDE functionality

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App!</h1>"

#Create Contact
@app.route("/create_contacts" , methods = ["POST"])
def create_contact():
    first_name = request.json.get('firstName')
    last_name = request.json.get('lastName')
    email = request.json.get('email')
    
    if not first_name or not last_name or not email:
        return {
            jsonify({"message": "You must include a first name, last name and email"}),
            400,
        }
    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)
    
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e :
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

#get contacts
@app.route('/contacts' , methods =['GET'])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(),contacts))
    
    return jsonify({"contacts" : json_contacts})
    

#update contact
@app.route('/update_contacts/<int:user_id>', methods =["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact :
        return jsonify({"message": "user not found"}),404
    
    data = request.json
    contact.first_name = data.get('firstName', contact.first_name)
    contact.last_name = data.get('lastName', contact.last_name)
    contact.email = data.get("email", contact.last_name)
    
    db.session.commit()
    
    return jsonify({"message " : "User Updated"}), 200

#delete contact
@app.route("/delete_contacts/<int:user_id>", methods = ["DELETE"])
def del_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact :
        return jsonify({"message": "user not fount"}),404
    
    db.session.delete(contact)
    db.session.commit()
    return jsonify({"message": "user deleted"}),200
    
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    app.run(debug = True)