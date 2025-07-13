import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler

# Токен вашего бота (замените на ваш токен)
TOKEN = "7763299534:AAHRHKUkzrNAJb9C5pmknsn3yalHzmJKHVQ"

# Папка для сохранения фотографий
SAVE_FOLDER = "/lists"
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Состояния диалога
PHOTO, CODE = range(2)


def start(update: Update, context: CallbackContext) -> None:
    """Отправляет приветственное сообщение при команде /start."""
    update.message.reply_text('Привет! Отправь мне фотографию, и я сохраню её на сервер.')


def handle_photo(update: Update, context: CallbackContext) -> int:
    """Обрабатывает полученные фотографии и запрашивает код."""
    # Сохраняем фото во временные данные пользователя
    photo_file = update.message.photo[-1].get_file()
    context.user_data['photo_file'] = photo_file

    # Просим пользователя ввести код
    update.message.reply_text('Фото получено! Теперь введи код, к которому оно относится:')

    # Переходим в состояние ожидания кода
    return CODE


def handle_code(update: Update, context: CallbackContext) -> int:
    """Обрабатывает введённый код и сохраняет фото."""
    user_code = update.message.text.strip()
    if len(user_code)!=3:
        print('Код как на бумаге, 3 цифры. Попробуйте заново')
        return ConversationHandler.END
    photo_file = context.user_data.get('photo_file')

    if not photo_file:
        update.message.reply_text('Ошибка: фото не найдено. Попробуй ещё раз.')
        return ConversationHandler.END

    # Формируем имя файла: код + оригинальный ID фото
    file_path = os.path.join(f'Lists/{user_code}', f"{user_code}_raw.jpg")

    # Скачиваем и сохраняем фотографию
    photo_file.download(file_path)

    update.message.reply_text(f'Фото сохранено с кодом "{user_code}" в файле: {file_path}')

    # Очищаем временные данные
    context.user_data.clear()

    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext) -> int:
    """Отменяет текущий диалог."""
    update.message.reply_text('Действие отменено. Можешь начать заново, отправив фото.')
    context.user_data.clear()
    return ConversationHandler.END


def main() -> None:
    """Запускает бота."""
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    # Настройка ConversationHandler для диалога
    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.photo, handle_photo)],
        states={
            CODE: [MessageHandler(Filters.text & ~Filters.command, handle_code)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(conv_handler)

    updater.start_polling()
    print("Бот запущен...")
    updater.idle()


if __name__ == '__main__':
    main()
