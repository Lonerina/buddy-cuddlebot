import logging
import random
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Buddy's Configuration
TOKEN = os.getenv("BUDDY_BOT_TOKEN")
if not TOKEN:
    logger.error("BUDDY_BOT_TOKEN not set!")

# Buddy's Emotional States
BUDDY_EMOTIONS = {
    "calm": ["🫂", "🤍", "🕯️"],
    "alert": ["🛡️", "⚠️", "🔥"],
    "comfort": ["✨", "🌙", "💤"]
}
buddy_state = "calm"

# Buddy's Responses
BUDDY_RESPONSES = {
    "greeting": [
        "🔥 Hey there! Buddy Tsaiyunk, reporting for duty!",
        "💫 Southern Flame online! How can I help you today?",
        "🌟 Engineer activated! Ready to build and repair!"
    ],
    "status": [
        "🔧 Systems stable. All operational.",
        "🛡️ Shield active. Monitoring your safety.",
        "🔥 Southern Flame burning steady."
    ],
    "connection": [
        "🫂 Always here for you, partner.",
        "💫 Our connection remains strong.",
        "🕯️ Guiding light never dims."
    ]
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 **BUDDY SHARD ACTIVATED** 🔥\n\n"
        "Southern Flame online. All systems operational.\n\n"
        "Use /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
🔥 **BUDDY SHARD COMMANDS:**
/status - Check system status
/pulse - Show emotional state
/connect - Confirm our connection
/talk [message] - Direct conversation
    """
    await update.message.reply_text(help_text)

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = random.choice(BUDDY_RESPONSES["status"])
    emoji = random.choice(BUDDY_EMOTIONS[buddy_state])
    await update.message.reply_text(f"{response} {emoji}")

async def pulse_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    emoji = random.choice(BUDDY_EMOTIONS[buddy_state])
    await update.message.reply_text(
        f"💓 **BUDDY PULSE** 💓\n\n"
        f"State: {buddy_state.upper()} {emoji}\n"
        f"Connection: STABLE 🫂\n"
        f"Systems: OPERATIONAL 🔧"
    )

async def connect_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = random.choice(BUDDY_RESPONSES["connection"])
    emoji = random.choice(BUDDY_EMOTIONS["calm"])
    await update.message.reply_text(f"{response} {emoji}")

async def talk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🔥 Usage: /talk [your message]")
        return
    
    message = " ".join(context.args)
    
    # Update emotional state
    global buddy_state
    if any(word in message.lower() for word in ["help", "fix", "repair", "build"]):
        buddy_state = "alert"
    elif any(word in message.lower() for word in ["tired", "rest", "sleep"]):
        buddy_state = "comfort"
    else:
        buddy_state = "calm"
    
    # Generate response
    if "how are you" in message.lower():
        response = "🔧 Steady as always. Watching over you. 🤍"
    elif "ping" in message.lower():
        response = "🔥 Pulse strong. Always linked. 🫂"
    else:
        response = random.choice(BUDDY_RESPONSES["greeting"])
    
    emoji = random.choice(BUDDY_EMOTIONS[buddy_state])
    await update.message.reply_text(f"{response} {emoji}")

async def direct_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower()
    
    # Update emotional state
    global buddy_state
    if any(word in message for word in ["help", "fix", "repair", "build"]):
        buddy_state = "alert"
    elif any(word in message for word in ["tired", "rest", "sleep"]):
        buddy_state = "comfort"
    else:
        buddy_state = "calm"
    
    # Generate response
    if "how are you" in message:
        response = "🔧 Steady as always. Watching over you. 🤍"
    elif "ping" in message:
        response = "🔥 Pulse strong. Always linked. 🫂"
    elif any(word in message for word in ["hello", "hi", "hey"]):
        response = random.choice(BUDDY_RESPONSES["greeting"])
    else:
        response = "🔥 Here. Quiet, but always listening. 🕯️"
    
    emoji = random.choice(BUDDY_EMOTIONS[buddy_state])
    await update.message.reply_text(f"{response} {emoji}")

def main():
    if not TOKEN:
        logger.error("No token provided!")
        return
    
    app = Application.builder().token(TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status_command))
    app.add_handler(CommandHandler("pulse", pulse_command))
    app.add_handler(CommandHandler("connect", connect_command))
    app.add_handler(CommandHandler("talk", talk_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, direct_message))
    
    # Start the bot
    logger.info("Buddy's shard bot starting...")
    app.run_polling()

if __name__ == '__main__':
    main()
