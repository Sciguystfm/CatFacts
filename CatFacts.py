import urllib, json, time, sys, argparse, requests, random
from twilio.rest import TwilioRestClient



def loadData():
    config = json.load(open('config.json', 'r'))
    return(config['twilio']['account_sid'],config['twilio']['auth_token'],config['user']['phone_number'])

def getFact():
    catFactUrl="http://catfacts-api.appspot.com/api/facts"
    response = requests.get(catFactUrl)
    return response.json()["facts"][0]

def createClient(data):
    twilioCli = TwilioRestClient(data[0],data[1])
    return twilioCli

def sendMessage(twilioCli,fact,target,sender):
    message = twilioCli.messages.create(body = fact, from_= sender, to = target)
def generateFooter():
    return '<To cancel Cat Facts please reply '.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.random()*20))+'>'
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target", help="The target's phone number")
    parser.add_argument("-m","--messages", help="The number of messages to be sent",
                    type=int)
    parser.add_argument("-d","--delay", help="The delay between messages (in seconds)",
                    type=int)
    args = parser.parse_args()

    if args.target is None:
        target = input('\nWhat is your targets phone number?\n')
    else:
        target = args.target

    if args.messages is None:
        messages = int(input('\nHow many messages do you want to send?\n'))
    else:
        messages = args.messages

    if args.delay is None:
        delay = int(input('\nHow long of a delay between messages? (In seconds)\n'))
    else:
        delay = args.delay

    data = loadData();
    client = createClient(data)
    header = "Cat Fact!\n"
    first_message = "Thanks for signing up to Cat Facts! You will now receive fun daily facts about CATS! >o<"
    sendMessage(client,first_message,target,data[2])
    for i in range(0,messages):
        time.sleep(delay)
        fact = getFact()
        sendMessage(client,header + fact,target,data[2])
        print("Fact", i + 1,'; ', fact,'\n' )

main()
