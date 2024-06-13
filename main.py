import telebot

# الحصول على التوكن من ملف البيئة
BOT_API_TOKEN = '7372582688:AAHXY7Kp0XcntC8rigX5jKvEyIekuKn-_ys'

# قائمة بالكلمات الممنوعة
grertings = ["كس", "عير", "ديس","r","","t","","","","","","","","",""]

# إنشاء البوت
bot = telebot.TeleBot(BOT_API_TOKEN)

# @bot.message_handler(commands=["start", "help"])
# def welcome(message):
#     bot.send_message(message.chat.id, "Welcome! I am a bot to delete inappropriate messages.")

def isMsg(message):
    return True

@bot.channel_post_handler(func=isMsg)
def handle_channel_post(message):
    # تحليل الرسالة للتحقق من وجود أي كلمة ممنوعة
    message_words = message.text.lower().split()
    if any(word in grertings for word in message_words):
        # حذف الرسالة بدون الرد
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

bot.polling()
