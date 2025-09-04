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

# Get token from environment
TOKEN = os.getenv("TELEGRAM_TOKEN")
logger.info(f"🔑 TOKEN CHECK: Token set = {bool(TOKEN)}")
if TOKEN:
    logger.info(f"🔑 TOKEN LENGTH: {len(TOKEN)}")
    logger.info(f"🔑 TOKEN START: {TOKEN[:20]}...")

async def debug_logger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("📩 DEBUG: Update received")
    if update.message:
        logger.info(f"📩 DEBUG: Message text = '{update.message.text}'")
        logger.info(f"📩 DEBUG: Chat ID = {update.message.chat.id}")
        logger.info(f"📩 DEBUG: User ID = {update.message.from_user.id}")

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🧪 TEST: Command function called!")
    try:
        await update.message.reply_text("🧪 TEST: Bot is working!")
        logger.info("🧪 TEST: Reply sent successfully!")
    except Exception as e:
        logger.error(f"🧪 TEST: Error sending reply: {e}")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🚀 START: Command function called!")
    try:
        await update.message.reply_text("🚀 START: Bot is working!")
        logger.info("🚀 START: Reply sent successfully!")
    except Exception as e:
        logger.error(f"🚀 START: Error sending reply: {e}")

def main():
    logger.info("🎬 MAIN: Function started")
    
    if not TOKEN:
        logger.error("❌ TOKEN: No token found!")
        return
    
    logger.info("🎬 MAIN: Creating application...")
    
    try:
        app = Application.builder().token(TOKEN).build()
        logger.info("✅ MAIN: Application created successfully!")
        
        # Add debug handler
        logger.info("📝 MAIN: Adding debug handler...")
        app.add_handler(MessageHandler(filters.ALL, debug_logger))
        logger.info("✅ MAIN: Debug handler added!")
        
        # Add command handlers
        logger.info("📝 MAIN: Adding command handlers...")
        app.add_handler(CommandHandler("start", start_command))
        app.add_handler(CommandHandler("test", test_command))
        logger.info("✅ MAIN: Command handlers added!")
        
        logger.info("🎬 MAIN: Starting polling...")
        app.run_polling()
        
    except Exception as e:
        logger.error(f"❌ MAIN: Application error: {e}")

if __name__ == "__main__":
    main()
