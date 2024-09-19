# from flask import Flask, request
from telegram import Update
from dispatcher import bot, dispatcher as dp
from telegram.ext import Updater

# app = Flask(__name__)
# @app.route("/webhook", methods=['POST'])
# def get_webhook():
#     update = Update.de_json(request.get_json(force=True), bot)
#     dp.process_update(update)
#     return {"result": "ok"}




def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7016866044:AAGjCKp8EiQsHb7Ems0SNuTcfME5WJ9H0Zo")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()