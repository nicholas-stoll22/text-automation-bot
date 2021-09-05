from twilio.rest import Client
import random, schedule, time

# preset message bank

good_night_bank = [
    "Goodnight",
    "goodnight",
    "night",
    "Night",]

# target phone and twilio number variable info
# in implementation, they would not be strings
# put your info in as ints

cellphone = ""
twilio_number = ""

# send a random message from bank

def send_message(quotes_list=good_night_bank):
    account = ""
    token = ""
    client = Client(account,token)
    quote = quotes_list[random.randint(0, len(quotes_list)-1)]

    client.messages.create(to=cellphone,
                            from_=twilio_number,
                            body=quote)

# schedule message to send at a certain time

schedule.every().day.at("20:00").do(send_message,good_night_bank)

while True:
    schedule.run_pending()
    time.sleep(2)