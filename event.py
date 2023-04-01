from flask import abort, make_response, jsonify
from db import Session, Event
session = Session()

def convert_dict(event):
    user_dict = {
                    'event_id': event.event_id,
                    'event_title': event.event_title,
                    'event_description': event.event_description,
                    'event_date': event.event_date,
                    'user_id': event.user_id
                }
    return user_dict


def create_event(event):
    
    try:
        event_title = event.get("event_title")
        event_description = event.get("event_description")
        event_date = event.get("event_date")
        user_id = event.get("user_id")
        a_event = Event(event_title= event_title, event_description = event_description, event_date = event_date, user_id = user_id)
        session.add(a_event)
        session.commit()        
        event_dict = convert_dict(a_event)
        return jsonify(event_dict)
    except Exception as e:
        print(e)

def read_event(event_id):    
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        
        event_dict = convert_dict(event)
        return jsonify(event_dict)
    except Exception as e:
        print(e)

def read_all_events(user_id):
    try:
        events = session.query(Event).filter_by(user_id=user_id)
        events_list = []
        if events:
            for event in events:
                events_dict = convert_dict(event)
                events_list.append(events_dict)
        return jsonify(events_list)
    except Exception as e:
        print(e)

def update_event(event):
    try:
        event_id = event.get("event_id")
        event_title = event.get("event_title")
        event_description = event.get("event_description")
        event_date = event.get("event_date")
        event = session.query(Event).filter_by(event_id=event_id).first()
        event.event_title = event_title
        event.evet_description = event_description
        event.event_date = event_date
        session.commit() 
        event_dict = convert_dict(event)
        return jsonify(event_dict)
    except Exception as e:
        print(e)

def delete_event(event_id):
    try:
        event = session.query(Event).filter_by(event_id=event_id).first()
        session.delete(event)
        session.commit()
        user_dict = convert_dict(event)
        return jsonify(user_dict)
    except Exception as e:
        print(e)