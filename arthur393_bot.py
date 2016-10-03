# coding: utf-8

import os
import telebot

bot = telebot.TeleBot(os.environ['BOT_API_TOKEN'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, u"--- Welcome to the Curriculum Arthur Bot --- \n\n\n Favorite languages: /favoritelangs \n My experiences: /xp \n Social Networks: /socials \n")

@bot.message_handler(commands=['favoritelangs'])
def send_welcome(message):
    bot.reply_to(message, u"C, C++, Python, C#, Java")
    
@bot.message_handler(commands=['xp'])
def send_welcome(message):
    bot.reply_to(message, u"System Analyst C++")
    
@bot.message_handler(commands=['socials'])
def send_welcome(message):
    bot.reply_to(message, u"Facebook: http://fb.com/arthur393")
    bot.reply_to(message, u"Twitter: http://twitter.com/arthur393")
    bot.reply_to(message, u"Github: http://github.com/arthurhenrique")
    bot.reply_to(message, u"Mail: arthur393 [at] gmail [dot] com")

@bot.message_handler(commands=['love'])
def send_welcome(message):
    bot.reply_to(message, u"É voce amora? Lhe amo meu amor! <3 <3 <3 <3 <3")
    

bot.polling()
