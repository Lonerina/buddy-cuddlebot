import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Debug logger
async def debug_logger(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"📩 Update received: {update}")

# Simple test command
async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🔥 Test command triggered!")
    await update.message.reply_text("✅ Test command works!")

# Home signal command
async def home_signal_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🔥 Home Signal command triggered!")
    await update.message.reply_text("⚡ Home Signal received!")

# Nyx command
async def nyx_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🌙 Nyx command triggered!")
    await update.message.reply_text("🌙 Nyx works!")

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info("🌟 Start command triggered!")
    await update.message.reply_text("🌟 Bot is working!")

# Main function
def main():
    # Get token from environment variable
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        logger.error("❌ No TELEGRAM_TOKEN found in environment variables!")
        return
    
    logger.info("🤖 Starting bot...")
    
    # Create application
    app = Application.builder().token(token).build()
    
    # Debug handler - logs all updates
    app.add_handler(MessageHandler(filters.ALL, debug_logger))
    
    # Register basic handlers
    logger.info("📝 Registering handlers...")
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("test", test_command))
    app.add_handler(CommandHandler("homesignal", home_signal_command))
    app.add_handler(CommandHandler("nyx", nyx_command))
    logger.info("✅ Handlers registered successfully!")
    
    # Start the bot
    logger.info("🚀 Starting polling...")
    app.run_polling()

if __name__ == "__main__":
    main()
