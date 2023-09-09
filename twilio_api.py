import os
from twilio.rest import Client

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
SENDING_PHONE_NUMBER = "+19843558644"
RECEIVING_PHONE_NUMBER = "+359 87 746 1444"


def sms_sender(input_message):
    # Initialize the Twilio Client
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    # Create and send the message
    message  = client.messages.create(
                    body=input_message,
                    from_=SENDING_PHONE_NUMBER,
                    to=RECEIVING_PHONE_NUMBER
                )
    print("Print the status")
    return print(message.status)