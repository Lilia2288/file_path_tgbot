from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Шлях до текстового файлу
FILE_PATH = "messages.txt"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привіт! Надсилай мені повідомлення, і я їх збережу у файл. Напиши /read, щоб побачити весь вміст файлу."
    )

async def save_message(update: Update, context: CallbackContext):
    message = update.message.text
    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write(message + "\n")  # Використовується новий рядок
    await update.message.reply_text("Повідомлення збережено!")

async def read_file(update: Update, context: CallbackContext):
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            content = file.read()
        if content:
            await update.message.reply_text("Ось вміст файлу:\n" + content)  # Використовується новий рядок
        else:
            await update.message.reply_text("Файл порожній.")
    except FileNotFoundError:
        await update.message.reply_text("Файл ще не створено.")

def main():
    # Вставте свій токен бота
    TOKEN = "8110024487:AAFVbx6oqPfF4NELDU4vWHnp9K7Nb24-WEQ"

    application = Application.builder().token(TOKEN).build()

    # Команди
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("read", read_file))

    # Обробка повідомлень
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_message))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()


# 8110024487:AAFVbx6oqPfF4NELDU4vWHnp9K7Nb24-WEQ

"""
синхронний код
"""