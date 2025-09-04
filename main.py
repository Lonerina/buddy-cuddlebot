import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
MODE = os.getenv("TELEGRAM_BOT_MODE", "polling")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🚀 START HANDLER TRIGGERED!")
    await update.message.reply_text("🚀 Bot is working!")

async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🧪 TEST HANDLER TRIGGERED!")
    await update.message.reply_text("🧪 Test works!")

def main():
    logger.info(f"🎬 MODE: {MODE}")
    
    if not TOKEN:
        logger.error("❌ NO TOKEN!")
        return
    
    app = Application.builder().token(TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test))
    
    if MODE == "webhook":
        logger.info("🌐 USING WEBHOOK MODE")
        # Webhook mode (no conflicts)
        port = int(os.environ.get('PORT', 8443))
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=os.environ.get('RAILWAY_SERVICE_NAME', '')
        )
    else:
        logger.info("📡 USING POLLING MODE")
        # Polling mode (conflicts if multiple instances)
        app.run_polling()

if __name__ == "__main__":
    main()
