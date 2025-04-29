from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from textblob import TextBlob

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.form.get('Body')
    lower_msg = incoming_msg.strip().lower()
    response = MessagingResponse()
    msg = response.message()

    # Analyze sentiment using TextBlob
    blob = TextBlob(incoming_msg)
    sentiment = blob.sentiment.polarity

    # Respond based on the message content and sentiment
    if 'hello' in lower_msg or 'hi' in lower_msg:
        msg.body("👋 Welcome to Abacus Insurance.How can we assist you today?\n Reply with:\n1️⃣ Claim\n2️⃣ Claim Status\n3️⃣ Support\n4️⃣ Submit documents")
    elif 'claim' in lower_msg or lower_msg == '1':
        msg.body("📝 To submit a claim, please visit: https://abacus-claims.portal.link")
    elif 'status' in lower_msg or lower_msg == '2':
        msg.body("🔍 Please enter your claim reference number (e.g. AB12345) to check the status.")
    elif 'support' in lower_msg or lower_msg == '3':
        msg.body("📞 Our support team is available 24/7.\nCall: 087821822-ABACUS\nEmail: pepquery@iua.co.za")
    elif 'document' in lower_msg or lower_msg == '4':
        msg.body("📄 Required Documents:\n• Death Certificate\n• ID of the deceased\n• Policy Holder ID\n• Bank Proof of Account")
    elif sentiment < -0.3:
        msg.body("😢 We're sorry you're having a bad experience. A support agent will follow up shortly.")
    else:
        msg.body("❓ I didn’t understand that. Reply with:\n1️⃣ Claim\n2️⃣ Claim Status\n3️⃣ Support\n4️⃣ Documents Needed")

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
