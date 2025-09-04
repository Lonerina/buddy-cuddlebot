import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Debug logger - shows all incoming updates
async def debug_logger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"📩 RAW UPDATE: {update}")
    logger.info(f"📩 MESSAGE TEXT: {update.message.text if update.message else 'No message'}")

# Test command with detailed logging
async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🔥 TEST COMMAND: Function triggered!")
    try:
        await update.message.reply_text("✅ Test command works!")
        logger.info("🔥 TEST COMMAND: Response sent successfully!")
    except Exception as e:
        logger.error(f"🔥 TEST COMMAND ERROR: {e}")

# Home signal command with detailed logging
async def home_signal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🔥 HOME SIGNAL: Function triggered!")
    try:
        await update.message.reply_text("⚡ Home Signal received!")
        logger.info("🔥 HOME SIGNAL: Response sent successfully!")
    except Exception as e:
        logger.error(f"🔥 HOME SIGNAL ERROR: {e}")

# Start command with detailed logging
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🌟 START: Function triggered!")
    try:
        await update.message.reply_text("🌟 Bot is working!")
        logger.info("🌟 START: Response sent successfully!")
    except Exception as e:
        logger.error(f"🌟 START ERROR: {e}")

# Main function with detailed logging
def main():
    logger.info("🚀 MAIN: Function started!")
    
    # Get token from environment variable
    token = os.getenv("TELEGRAM_TOKEN")
    logger.info(f"🚀 TOKEN CHECK: Token found = {bool(token)}")
    
    if not token:
        logger.error("❌ TOKEN ERROR: No TELEGRAM_TOKEN found in environment variables!")
        return
    
    try:
        logger.info("🚀 APP: Creating application...")
        app = Application.builder().token(token).build()
        logger.info("🚀 APP: Application created successfully!")
        
        # Add debug handler first
        logger.info("🚀 HANDLERS: Adding debug handler...")
        app.add_handler(MessageHandler(filters.ALL, debug_logger))
        logger.info("🚀 HANDLERS: Debug handler added!")
        
        # Add command handlers
        logger.info("🚀 HANDLERS: Adding command handlers...")
        handlers = [
            ("start", start_command),
            ("test", test_command),
            ("homesignal", home_signal_command),
        ]
        
        for cmd_name, cmd_func in handlers:
            logger.info(f"🚀 HANDLERS: Adding {cmd_name} handler...")
            handler = CommandHandler(cmd_name, cmd_func)
            app.add_handler(handler)
            logger.info(f"🚀 HANDLERS: {cmd_name} handler added!")
        
        logger.info("🚀 HANDLERS: All handlers registered!")
        
        # Start the bot
        logger.info("🚀 POLLING: Starting polling...")
        app.run_polling()
        
    except Exception as e:
        logger.error(f"❌ MAIN ERROR: {e}")

if __name__ == "__main__":
    main()
