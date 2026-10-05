from telegram import Bot

async def send_telegram_notification(settings, message):
    if not settings or not settings.get("enabled", False):
        return

    token = settings.get("token")
    chat_id = settings.get("chat_id")
    placeholders = {"your token id", "your chat id"}
    if (
        not token
        or not chat_id
        or str(token).strip().lower() in placeholders
        or str(chat_id).strip().lower() in placeholders
    ):
        print("Telegram notification skipped: set a valid token and chat_id in config/config.yaml")
        return

    try:
        async with Bot(token=token) as bot:
            await bot.send_message(chat_id=chat_id, text=message)
    except Exception as error:
        print(f"Telegram notification failed: {error}")
