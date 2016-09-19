import urllib, json, time, sys, argparse, requests
from twilio.rest import TwilioRestClient



def loadCredentials():
    config = json.load(open('config.json', 'r'))
    return(config['twilio']['account_sid'],config['twilio']['auth_token'])

def getFact():
    catFactUrl="http://catfacts-api.appspot.com/api/facts"
    response = requests.get(catFactUrl)
    return response.json()["facts"][0]

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
        messages = input('\nHow many messages do you want to send?\n')
    else:
        messages = args.messages

    if args.delay is None:
        delay = input('\nHow long of a delay between messages? (In seconds)\n')
    else:
        delay = args.delay

main()
