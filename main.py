from base import api
import time
import random

answers = [a.replace('\n', '') for a in open('answers.txt', 'r').readlines()]


while 1:
    a = api.wall.getComments(owner_id='-174782021', post_id='881', sort='desc', count='1', preview_length='1', v='5.92')
    if time.time()-a['items'][0]['date'] > 300 and a['items'][0]['from_id'] != api.users.get(v=5.92)[0]['id']:
        api.wall.createComment(owner_id='-174782021', post_id='881', message=answers[random.randint(0, len(answers)-1)])
    time.sleep(5)
