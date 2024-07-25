# Создаем функцию с двумя параметрами

def send_email(massage, recipient, *, sender = "university.help@gmail.com"):
    if '@' not in recipient and '@' not in sender:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif not ((recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')) and (
                    sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
