# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console

account_sid = 'AC39d63f16b6800309002387c6116cb01b'
auth_token = '7103864073a005490cd1cb635bd4253e'
client = Client(account_sid, auth_token)


message = client.messages.create(
                              from_='+15732852873',
                              body='You have registered an appointment at OPD, abc centre with token number "abcdef". The predicted time for your turn is around hh: mm on dd/mm/yy  ',
                              #status_callback='http://postb.in/1234abcd',
                              to='+919140876468'
                          )

print(message.sid)




