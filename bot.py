import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from convert import convert_to_circle

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video or update.message.document
    if not video:
        await update.message.reply_text("Пришли мне видео.")
        return

    file = await context.bot.get_file(video.file_id)
    input_path = "input.mp4"
    output_path = "circle.mp4"
    
    await file.download_to_drive(input_path)
    convert_to_circle(input_path, output_path)

    await update.message.reply_video_note(video_note=open(output_path, "rb"))
    os.remove(input_path)
    os.remove(output_path)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.VIDEO | filters.Document.VIDEO, handle_video))
    app.run_polling()

