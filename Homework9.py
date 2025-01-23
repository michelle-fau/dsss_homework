import logging
import os
from dotenv import load_dotenv
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Hugging Face API setup
HUGGINGFACE_API_KEY = os.environ.get("HUGGINGFACE_API_KEY")
HUGGINGFACE_MODEL = "tiiuae/falcon-7b-instruct"  # Use Falcon-7B-Instruct model


# Define a command handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
       Sends a welcome message when the /start command is invoked.
    """
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Hi! I'm a bot powered by an LLM. How can I help you?")


# Helper function to query Hugging Face API
def query_huggingface_api(prompt: str):
    """
        Sends a prompt to the Hugging Face API and retrieves the generated response.

        Args:
            prompt (str): The input prompt for the language model.

        Returns:
            str: The generated response from the model or an error message.
    """

    # Define the API URL and headers
    url = f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL}"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

    # Prepare payload
    data = {"inputs": prompt, "parameters": {"temperature": 0.5, "max_new_tokens": 150}}

    # Make request to Hugging Face API
    response = requests.post(url, headers=headers, json=data)

    # Handle the API response
    if response.status_code == 200:
        output = response.json()
        return output[0]["generated_text"]
    else:
        return f"Error: {response.status_code} - {response.text}"


# Define a handler for processing user messages
async def ai_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
        Handles user messages, sends them to the Hugging Face API, and returns the generated response.

        Args:
            update (Update): Telegram update containing the user's message.
            context (ContextTypes.DEFAULT_TYPE): Context object containing metadata about the chat.
    """

    # Get the user's message
    message = update.effective_message.text

    # Query the Hugging Face API with the message
    response = query_huggingface_api(message)

    # Send the generated response back to the user
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


def main():
    # Create the Telegram bot application using the bot token from environment variables
    application = ApplicationBuilder().token(os.environ["TELEGRAM_TOKEN"]).build()

    # Define the /start command handler
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # Define the message handler for text messages
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, ai_chat)
    application.add_handler(message_handler)

    # Start the bot's polling loop
    application.run_polling()


if __name__ == "__main__":
    main()
    