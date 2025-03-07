from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
import os 

# Load environment variables from.env file
load_dotenv()

# Replace with your actual bot token
TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: CallbackContext) -> None:
    """Sends a welcome message when the /start command is issued."""
    await update.message.reply_text("Hello! I'm an Echo Bot 🤖. Send me a message, and I'll repeat it!")

async def echo(update: Update, context: CallbackContext) -> None:
    """Repeats the user’s message."""
    user_message = update.message.text
    await update.message.reply_text(user_message)

def main():
    """Main function to start the bot."""
    app = Application.builder().token(TOKEN).build()

    # Command handler for /start
    app.add_handler(CommandHandler("start", start))

    # Message handler to echo messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
