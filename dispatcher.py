from telegram.ext import Dispatcher, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import Bot
from handlers import commands, registration
import states

bot = Bot(token="7016866044:AAGjCKp8EiQsHb7Ems0SNuTcfME5WJ9H0Zo")
dispatcher = Dispatcher(bot, None, workers=0)

dispatcher.add_handler(CommandHandler("start", commands.start))
dispatcher.add_handler(CommandHandler("help", commands.help))
dispatcher.add_handler(CommandHandler("contact", commands.contact))


dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            CommandHandler("register", commands.register)
        ],
        states={
            states.FULLNAME: [
                MessageHandler(Filters.all, registration.get_fullname)
            ],
            states.AGE: [
                MessageHandler(Filters.all, registration.get_age)
            ],
            states.CONTACT: [
                MessageHandler(Filters.all, registration.get_contact)
            ],
            states.LOCATION: [
                MessageHandler(Filters.location, registration.get_location)
            ]
        },
        fallbacks=[
            CommandHandler("help", commands.help)
        ]
    )
)