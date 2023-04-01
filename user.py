from flask import abort, make_response, jsonify
from db import Session, User
session = Session()

def convert_dict(user):
    user_dict = {
                    'user_id': user.user_id,
                    'user_email': user.user_email,
                    'user_password': user.user_password,
                    'user_name': user.user_name,
                }
    return user_dict

def register_user(user):
    try:
        user_name = user.get("user_name")
        user_email = user.get("user_email")
        user_password = user.get("user_password")

        user = User(user_name= user_name, user_email = user_email, user_password = user_password, user_status = 0)
        session.add(user)
        session.commit()
        user_dict = convert_dict(user)
        return jsonify(user_dict)
    except Exception as e:
        print(e)

def login(user):
    try:
        user_email = user.get("user_email")
        user_password = user.get("user_password")
        user = session.query(User).filter_by(user_password=user_password, user_email = user_email).first()
        if user is not None:
            user.user_status = 1
            session.commit()
            user_dict = convert_dict(user)
            return jsonify(user_dict)
        else:
            return jsonify({})
        
    except Exception as e:
        print(e)

def logout(user_id):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        user.user_status = 0
        session.commit()
        user_dict = convert_dict(user)
        if user is None:
            abort(404, f"User with ID {user_id} not found")
        return jsonify(user_dict)
    except Exception as e:
        print(e)

def read_user(user_id):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        user_dict = convert_dict(user)
        return jsonify(user_dict)
    except Exception as e:
        print(e)
    ""
def read_all_users():
    try:
        users = session.query(User).all()
        users_list = []
        if users:
            for user in users:
                user_dict = convert_dict(user)
                users_list.append(user_dict)
        return jsonify(users_list)
    except Exception as e:
        print(e) 

def update_user(user):
    try:
        user_id = user.get("user_id")
        user_name = user.get("user_name")
        user_email = user.get("user_email")
       

        user = session.query(User).filter_by(user_id=user_id)
        user.user_name = user_name
        user.user_email = user_email
        session.commit()
        return jsonify(user)
    except Exception as e:
        print(e)


def delete_user(user_id):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        session.delete(user)
        session.commit()
        user_dict = convert_dict(user)
        return jsonify(user_dict)
    except Exception as e:
        print(e)

