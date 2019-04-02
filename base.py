import vk


ACCESS_TOKEN = ''


def auth(access_token):
    session = vk.Session(access_token=access_token)
    api = vk.API(session)
    return api


api = auth(access_token=ACCESS_TOKEN)