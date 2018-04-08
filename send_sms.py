# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACb35ae9f2dd28d3896e7ab499f8fb11ca"
auth_token = "2192bfd2225f28aaa18b303a2bf07e86"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+13343442066",
    from_="+13474078801",
    body="Hello there!")
