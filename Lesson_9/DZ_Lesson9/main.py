# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from botCommands import *

app = ApplicationBuilder().token(
    "5873495757:AAGw-yrONOhtP0o3ArZX4oG0tu3yErvL1VM").build()

app.add_handler(CommandHandler("hello", hi_commands))
app.add_handler(CommandHandler("help", help_commands))
app.add_handler(CommandHandler("time", time_commands))
app.add_handler(CommandHandler("sum", sum_commands))
app.add_handler(CommandHandler("diff", diff_commands))
app.add_handler(CommandHandler("multi", multi_commands))
app.add_handler(CommandHandler("div", div_commands))
print('server start')
app.run_polling()


