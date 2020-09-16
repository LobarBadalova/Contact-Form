# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc6254ef7affe13dcc2abe70ce08e0da9'
auth_token = '0e6114f09342e7f188c506fa6f62a42e'
client = Client(account_sid, auth_token)

otp=random.randint(100000, 999999)
print(otp)
message = client.messages \
                .create(
                     body="Welcome to Cosmetology Website. Your code is"+str(otp),
                     from_='+17472277637',
                     to='+998944040855'
                 )

print(message.sid)