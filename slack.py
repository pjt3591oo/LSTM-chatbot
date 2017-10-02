# RTM
from slackclient import SlackClient
from slacker import Slacker
from botengine import make_reply
import time

slack_token = '발급받은 토큰'
sc = SlackClient(slack_token)

def notification(message):
    global slack_token
    slack = Slacker(slack_token)
    slack.chat.post_message('#general', message)

if sc.rtm_connect():
    print('slack Connected')
    while True:
        receive_data = sc.rtm_read()

        if len(receive_data):
            keys = list(receive_data[0].keys())

            if 'type' in keys and 'text' in keys and 'user' in keys:
                print(receive_data[0])
                message = receive_data[0]['text']
                try:
                    new_sentence = make_reply(message)
                    notification(new_sentence)
                except KeyError:
                    notification(message + ' 해당 말은 문장 생성이 안되요 ㅠㅠ')
                # TypeError
                # ValueError
        time.sleep(1)
else:
    print("Connection Failed")