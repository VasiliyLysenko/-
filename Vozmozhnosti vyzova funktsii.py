# Создаем функцию с двумя параметрами

def send_email(massage, recipient, sender = "university.help@gmail.com"):
    if ('@' not in recipient and '@' not in sender) or (recipient.endswith('.ru') and sender.endswith('.net')):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')