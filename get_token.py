import vk

LOGIN = ''
PASSWORD = ''
APP_ID = ''


def get_key():
    print(vk.AuthSession(app_id=APP_ID, user_login=LOGIN, user_password=PASSWORD,
                         scope='wall,offline').access_token)


print(get_key())
input('Для закрытия нажмите Enter...')
