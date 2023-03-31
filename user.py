# from flask import abort, make_response
from db import Session, User
session = Session()


def register(user):
    try:
        user_name = user.get("user_name")
        user_email = user.get("user_email")
        user_password = user.get("user_password")

        user = User(user_name= user_name, user_email = user_email, user_password = user_password, user_status = 0)
        session.add(user)
        session.commit()
    except Exception as e:
        print(e)

def login(user):
    try:
        user_email = user.get("user_email")
        user_password = user.get("user_password")
        sql = "SELECT user_id FROM user WHERE user_email = %s AND user_password = %s;"
        user = session.query(User).filter_by(user_password=user_password, user_email = user_email).first()
        user.user_status = 1
        session.commit()
        return user
    except Exception as e:
        print(e)

def logout(user):
    try:
        user_id = user.get("user_id")
        user = session.query(User).filter_by(user_id=user_id).first()
        user.user_status = 0
        session.commit()
        return True
    except Exception as e:
        print(e)

def read(user_id):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        return user
    except Exception as e:
        print(e)
    
def read_all():
    try:
        users = session.query(User).all()
        return users
    except Exception as e:
        print(e) 

def update(user):
    try:
        user_id = user.get("user_id")
        user_name = user.get("user_name")
        user_email = user.get("user_email")
        user_password = user.get("user_password")
       

        user = session.query(User).filter_by(user_id=user_id)
        user.user_name =user_name
        user.user_email = user_email
        user.user_password = user_password
        session.commit()
        
    except Exception as e:
        print(e)


def delete(user_id):
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
        session.delete(user)
        session.commit()
    except Exception as e:
        print(e)

