import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get token
TOKEN = os.getenv("TELEGRAM_TOKEN")
logger.info(f"🔑 TOKEN: {bool(TOKEN)}")

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🚀 START HANDLER TRIGGERED!")
    await update.message.reply_text("🚀 Bot is working!")

async def test_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🧪 TEST HANDLER TRIGGERED!")
    await update.message.reply_text("🧪 Test works!")

async def debug_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("📩 DEBUG: Received message")
    if update.message:
        logger.info(f"📩 DEBUG: Text = '{update.message.text}'")

def main():
    logger.info("🎬 MAIN STARTED")
    
    if not TOKEN:
        logger.error("❌ NO TOKEN!")
        return
    
    logger.info("🎬 CREATING APP...")
    app = Application.builder().token(TOKEN).build()
    
    logger.info("🎬 CREATING HANDLERS...")
    
    # Create handlers explicitly
    start_cmd = CommandHandler("start", start_handler)
    test_cmd = CommandHandler("test", test_handler)
    debug_cmd = MessageHandler(filters.ALL, debug_handler)
    
    logger.info("🎬 ADDING HANDLERS...")
    app.add_handler(start_cmd)
    logger.info("✅ START HANDLER ADDED")
    app.add_handler(test_cmd)  
    logger.info("✅ TEST HANDLER ADDED")
    app.add_handler(debug_cmd)
    logger.info("✅ DEBUG HANDLER ADDED")
    
    logger.info("🎬 STARTING POLLING...")
    app.run_polling()

if __name__ == "__main__":
    main()
