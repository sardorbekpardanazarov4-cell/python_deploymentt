import telebot
import time

# Replace 'YOUR_API_TOKEN' with your actual bot token
TOKEN = '8447708268:AAE3fnbAdAlIlficHVANA7pCdUrzGVUkNYc'
bot = telebot.TeleBot(TOKEN)

# Handler for the /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing? I am an echo bot! Send me anything.")

# Handler for all other text messages
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # This sends the user's message back to them
    bot.send_message(message.chat.id, "You wrote: " + message.text)

# Start the bot to continuously poll for new messages
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(15) # Sleep for a bit before retrying in case of an error
