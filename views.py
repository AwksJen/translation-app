from flask import Flask, request

from twilio import twiml

app = Flask(__name__)
# app.secret_key = os.getenv('SECRET_KEY', 'secretzzz')


# @app.route('/')
# def index():
#     """Show the index."""

#     return render_template('index.html')


@app.route('/sms', methods=['POST'])
def sms():
    """send sms"""
    # twilio response
    response = twiml.Response()
    # retrieve body of message
    body = request.form['Body']

    response.message("Hello World y or nay".format(body))

    return str(response)
