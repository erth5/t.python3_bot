# mastrobot_example.py
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# function to handle the /start command
def start(update, context):
    time.sleep(7.01)
    update.message.reply_text('start command received')


# function to handle the /help command
def help(update, context):
    update.message.reply_text('help command received')
    update.message.text('en')


# function to handle errors occured in the dispatcher
def error(update, context):
    update.message.reply_text('an error occurred')


# function to handle normal text
def text(update, context):
    text_received = update.message.text
    # time.sleep(7.01)
    print("text=" + update.message.text)
    print("chatID, updateID", update.message.chat_id, update.update_id)
    print()
    print(update.message)
    print()
    print(update.message.chat)
    print()
    print(update.message.reply_text("test"))
    update.message.reply_text(f'did you said "{text_received}" ?')

# function to handle reply's
def reply(update, context):
    update.message.reply_text('chicken wings')


def one_run(text):
    print(text)
    # TODO send message without update Object

def main():
    TOKEN = ""

    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialogue
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # rem(dispatcher.job_queue.start())
    dispatcher.add_handler(MessageHandler(Filters.reply, reply))

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # run it first
    one_run("human salary")

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()




if __name__ == '__main__':
    main()
