from telegram.ext import Dispatcher, Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext, PollHandler, PollAnswerHandler
from telegram import Bot, Update
from handlers import commands, registration, common, cart
import states

def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("7016866044:AAGjCKp8EiQsHb7Ems0SNuTcfME5WJ9H0Zo")
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", commands.start))
    dispatcher.add_handler(CommandHandler("help", commands.help))
    dispatcher.add_handler(CommandHandler("language", commands.language))
    dispatcher.add_handler(CommandHandler("contact", commands.contact))

    # dispatcher.add_handler(PollHandler(poll_handler))
    
    # # Handler for poll answers
    # dispatcher.add_handler(PollAnswerHandler(poll_answer_handler))

    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[
                MessageHandler(Filters.text("cart"), cart.view_cart)
            ],
            states={
                states.CART_ACTIONS: [
                    CallbackQueryHandler(cart.cart_action)
                ]
            },
            fallbacks=[
                dispatcher.add_handler(CommandHandler("start", commands.start))
            ]
        )
    )


    dispatcher.add_handler(
        ConversationHandler(
            entry_points=[
                MessageHandler(Filters.text("📚 Kitoblar"), common.get_books),
                MessageHandler(Filters.text("📚 Knigi"), common.get_books),
                MessageHandler(Filters.text("📚 Books"), common.get_books),
                MessageHandler(Filters.text("books"), common.get_books)
            ],
            states={
                states.BOOK_SINGLE: [
                    CallbackQueryHandler(common.get_book)
                ],
                states.BOOK_ACTION: [
                    CallbackQueryHandler(common.get_book_action)
                ],
                states.GET_ORDER: [
                    MessageHandler(Filters.text, common.get_book_order)
                ]
            },
            fallbacks=[
                CommandHandler("start", commands.start)
            ]
        )
    )
    dispatcher.add_handler(CallbackQueryHandler(common.set_language))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()



if __name__ == "__main__":
    main()