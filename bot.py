import telebot
import random

TOKEN = "8167075204:AAFv2_ArX-qLZ-1UxgNBWtFbQ_0S9ED8qWA"
bot = telebot.TeleBot(TOKEN)

user_balance = {}

def get_balance(uid):
    return user_balance.get(uid, 500)

def update_balance(uid, amount):
    user_balance[uid] = get_balance(uid) + amount

@bot.message_handler(commands=['start'])
def start(message):
    uid = message.from_user.id
    if uid not in user_balance:
        user_balance[uid] = 500
    bot.reply_to(message, "🔥 INFERMAXBOT v2.1 PRO AKTIF!\nGunakan /blackjack /coinflip /balance /store /profile /scan")

@bot.message_handler(commands=['balance'])
def balance(message):
    bal = get_balance(message.from_user.id)
    bot.reply_to(message, f"💰 Saldo kamu: {bal} InferCoins")

@bot.message_handler(commands=['blackjack'])
def blackjack(message):
    uid = message.from_user.id
    args = message.text.split()
    if len(args) != 2 or not args[1].isdigit():
        bot.reply_to(message, "Gunakan: /blackjack [jumlah taruhan]")
        return
    bet = int(args[1])
    if bet > get_balance(uid):
        bot.reply_to(message, "❌ Saldo tidak cukup.")
        return
    result = random.choice(["win", "lose"])
    if result == "win":
        update_balance(uid, bet)
        bot.reply_to(message, f"🂡 Kamu menang! +{bet} InferCoins")
    else:
        update_balance(uid, -bet)
        bot.reply_to(message, f"💀 Kamu kalah! -{bet} InferCoins")

@bot.message_handler(commands=['coinflip'])
def coinflip(message):
    uid = message.from_user.id
    args = message.text.split()
    if len(args) != 2 or not args[1].isdigit():
        bot.reply_to(message, "Gunakan: /coinflip [jumlah taruhan]")
        return
    bet = int(args[1])
    if bet > get_balance(uid):
        bot.reply_to(message, "❌ Saldo tidak cukup.")
        return
    result = random.choice(["win", "lose"])
    if result == "win":
        update_balance(uid, bet)
        bot.reply_to(message, f"🪙 HEADS! Menang +{bet} InferCoins")
    else:
        update_balance(uid, -bet)
        bot.reply_to(message, f"🪙 TAILS! Kalah -{bet} InferCoins")

@bot.message_handler(commands=['store'])
def store(message):
    bot.reply_to(message, "🛒 Darknet Store:\n- 100 💰 = Scan Boost\n- 500 💰 = Coin Doubler\n(Coming Soon)")

@bot.message_handler(commands=['profile'])
def profile(message):
    bal = get_balance(message.from_user.id)
    bot.reply_to(message, f"👤 Profile {message.from_user.first_name}\n💰 InferCoins: {bal}\n⚔️ Rank: Newbie\n🧬 Exp: 0")

@bot.message_handler(commands=['scan'])
def scan(message):
    bot.reply_to(message, "🔍 Memulai Recon...\n[+] Subdomain ditemukan!\n[+] Parameter terdeteksi...\n[✓] POTENSI BUG TERBACA!! 💥")

bot.polling()3
import telebot

TOKEN = '8167075204:AAFv2_ArX-qLZ-1UxgNBWtFbQ_0S9ED8qWA'  # Ganti dengan token asli
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, f"🔥 INFERMAXBOT V2.0 AKTIF 🔥\nSelamat datang, {message.from_user.first_name}!")

bot.polling()
