import urllib, json, time, sys, argparse, requests
from twilio.rest import TwilioRestClient


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target", help="The target's phone number")
    parser.add_argument("-m","--messages", help="The number of messages to be sent",
                    type=int)
    parser.add_argument("-d","--delay", help="The delay between messages (in seconds)",
                    type=int)
    parser.parse_args()

main()
