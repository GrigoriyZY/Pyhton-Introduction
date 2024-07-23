# Рассылка писем

# Функция проверки корректности адреса email
def is_valid(email):
    if '@' not in email:
        return False
    elif ".com" in email or ".net" in email or '.ru' in email:
        return True
    else:
        return False


# Функция сортировки писем
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if not is_valid(recipient):
        print(f'Невозможно отправить письмо на адрес {recipient}')
        return
    elif not is_valid(sender):
        print(f'Невозможно отправить письмо c адреса {sender}')
        return
    if recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        return
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        return
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        return


# Проверки работы функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.org')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
