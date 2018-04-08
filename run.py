from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio import twiml
from food import get_recipe
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """ """

    if request.method == 'GET':
        return 'None'
    elif request.method == 'POST':
        # Start our response
        resp = MessagingResponse()
        # Add a message
        #resp.message("Ahoy! Thanks so much for your message.") 
        
        myURL = request.form["MediaUrl0"]
        req = requests.get(myURL)
        image_URL = req.url
        resp.message(get_recipe(image_URL))
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
