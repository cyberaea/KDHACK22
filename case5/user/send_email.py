from django.core.mail import send_mail
def send_email(email):
    send_mail(
        subject='Бронь в Молодежном Центре', 
        message='До вашего мероприятия в Молодежном Центре Калининграда осталось меньше 24 часов', 
        from_email='youthcentre.klgd@gmail.com', 
        auth_password='bolshayabebra', 
        recipient_list=[email],
    )