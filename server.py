from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    app.run()
# from flask import Flask, request

# from twilio.twiml.messaging_response import MessagingResponse

# app = Flask(__name__)
# # app.secret_key = os.getenv('SECRET_KEY', 'secretzzz')


# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     """Respond to incoming calls with a simple text message."""
#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Add a message
#     resp.message("The Robots are coming! Head for the hills!")

#     return str(resp)


# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0")
#     app.run()
