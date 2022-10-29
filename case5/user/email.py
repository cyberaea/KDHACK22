from .models import User
from datetime import datetime
from .send_email import send_email

def email():
    u = User()
    date = u.date()
    email = u.email()
    approved = u.approved()
    if 24 >= datetime.now().hour - date.hour >= 23 and approved:
        return send_email(email)