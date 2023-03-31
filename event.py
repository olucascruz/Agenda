from db import Session, Event
session = Session()

def create(event):
    
    try:
        event_title = event.get("event_title", "")
        event_description = event.get("event_description", "")
        event_date = event.get("event_date", "")
        user_id = event.get("user_id", "")
        aevent = Event(event_title= event_title, event_description = event_description, event_date = event_date, user_id = user_id)
        session.add(aevent)
        session.commit()        
        
    except Exception as e:
        print(e)

def read(event_id):    
    try:
        user = session.query(Event).filter_by(event_id=event_id)
        return user
    except Exception as e:
        print(e)

def read_all(user_id):
    try:
        users = session.query(Event).filter_by(user_id=user_id)
        return users
    except Exception as e:
        print(e)

def update(event):
    try:
        event_id = event.get("event_id", "")
        event_title = event.get("event_title", "")
        event_description = event.get("event_description", "")
        event_date = event.get("event_date", "")
        event = session.query(Event).filter_by(event_id=event_id)
        event.event_title = event_title
        event.evet_description = event_description
        event.event_date = event_date
    except Exception as e:
        print(e)

def delete(event_id):
    return
    try:
        event = session.query(Event).filter_by(event_id=event_id)
    except Exception as e:
        print(e)