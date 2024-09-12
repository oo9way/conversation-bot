from flask import Flask, request
from telegram import Update
from dispatcher import bot, dispatcher as dp


app = Flask(__name__)
@app.route("/webhook", methods=['POST'])
def get_webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp.process_update(update)
    return {"result": "ok"}