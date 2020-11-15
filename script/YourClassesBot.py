import requests
import my_timings
from time import sleep
from datetime import datetime

TOKEN = "Your Telegram Bot Token" #OR you can call it SENDER 
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
print("\n\n Bot Started Successfully!")
while True:
    now = datetime.now()
    get_time = now.strftime("%H:%M")
    today = now.strftime("%A")

    if get_time == '11:00': #ASSIGN the time here of when you want to get the Message, Must be in Hours and Minutes.
        sent = 0
        while (sent == 0):
            def send_message(send_class, chat_id):
                url = URL + "sendMessage?text={}&chat_id={}".format(send_class, chat_id)
                requests.get(url)

            if today == 'Monday':
                send_class = my_timings.Monday
                sent = 1
            elif today == 'Tuesday':
                send_class = my_timings.Tuesday
                sent = 1
            elif today == 'Wednesday':
                send_class = my_timings.Wednesday
                sent = 1
            elif today == 'Thursday':
                send_class = my_timings.Thursday
                sent = 1
            elif today == 'Friday':
                send_class = my_timings.Friday
                sent = 1
            elif today == 'Saturday':
                send_class = my_timings.Saturday
                sent = 1
            elif today == 'Sunday':
                send_class = my_timings.Sunday
                sent = 1

            chat_id = "Chat ID" #RECEIVER's Chat ID
            send_message(send_class, chat_id)
            sleep(55)
    else:
        sleep(55)
