import logging, os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Debug logger
async def debug_logger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"📩 Update received: {update}")

# Simple /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌟 Bot alive & responsive!")

def main():
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("❌ TELEGRAM_TOKEN environment variable missing!")

    app = Application.builder().token(token).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("debug", debug_logger))

    # Webhook setup for Railway
    port = int(os.environ.get("PORT", 8443))
    url = os.getenv("RAILWAY_URL")
    if not url:
        raise RuntimeError("❌ RAILWAY_URL environment variable missing!")

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        url_path=token,
        webhook_url=f"https://{url}/{token}"
    )

if __name__ == "__main__":
    main()
