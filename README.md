# CatFacts
##### A fun little python script that will send cat facts to a friends phone.
##### [Inspired by this Reddit post](https://www.reddit.com/r/funny/comments/owx3v/so_my_little_cousin_posted_on_fb_that_he_was/)
<br />
### Dependencies
___
The script uses the Python libraries Requests and Twillo
* Requests
* Twilio
<br />

### Usage
___
**CatFacts.py [-h] [-t TARGET] [-m MESSAGES] [-d DELAY]**
```
Optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        The target's phone number
  -m MESSAGES, --messages MESSAGES
                        The number of messages to be sent
  -d DELAY, --delay DELAY
                        The delay between messages (in seconds)
```
<br />
### Config
___
##### The Config file should be formatted as below, and must be in the same directory as the script

_config.json_
```
{"twilio":
    {
      "account_sid":"affpoas8f98fa8sa9f8f0as08fsa0f8a0fs",
      "auth_token":"jafkljflkasjfkj2khj4lkh5rjkhg32"
    },
 "user":
    {
      "phone_number":"9999999999"
    }
}
```
