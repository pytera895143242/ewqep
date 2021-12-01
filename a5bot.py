from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 1045832338
id_chat= '-1001725761556'
voice_chat_id = -1001533221887

session_ids = [2138114850,2117293568,2109691120,
2111537384,2140054039,2143075798,
2104949535,2126724940,2121285225,
2133079225,2126250972,2115575454,
2102982104,2095771800,2118144794,
2104334929,2120884883,2143437907]

@app.on_message(filters.text)
async def payments (client,message):
    global id_chat
    if message.from_user.id == my_id and message.text == 'Аа':
        await app.edit_message_text(message_id=message.message_id,chat_id=message.chat.id,text="""Реквизиты для оплаты спринта, просто нажми и они сохранятся👌💃🏼

🇷🇺Сбербанк - <pre>4817760152002113</pre>

🇷🇺Тинькофф - <pre>5536914049813144</pre>

🇰🇬Mbank online - <pre>996772187870</pre>

🇰🇬Элсом - <pre>0770350099</pre>

🇺🇿Uzcard - <pre>8600120420267414</pre>

🇺🇦Monobank - <pre>4441114441436100</pre>

🇰🇿Каспи - <pre>77782085140</pre>

▫️Киви - <pre>79183561047</pre>
▫️Юмани  - <pre>410019301888334</pre>

Бонус на 24 часа: <b>Стоимость - 4.88$</b> 
🇷🇺 344 ₽
🇰🇬 422 сом
🇺🇿 52 400 сум 
🇺🇦 129 гривен
🇰🇿 2078 тенге
Курс если изменился, не проблема😉 меняй)) 

Если с другой страны, напиши с какой  решим)
Как оплатишь, чек, или скрин оплаты отправь мне 😎 
После добавлю тебя в спринт⚡️""",parse_mode='html')

        await app.copy_message(chat_id=message.chat.id,from_chat_id=voice_chat_id,message_id=16)


    if message.from_user.id == my_id and message.text == 'Пппп':
        await app.delete_messages(chat_id=message.chat.id,message_ids=message.message_id)
        id_user = message.chat.id
        try:
            await app.add_chat_members(chat_id=id_chat,user_ids=id_user)
            await app.send_message(chat_id=message.chat.id, text="""Еее 🥳🥳 всё, добавил тебя в спринт, 
Глянь чат, там тебе прислали обучение 👇""")
        except:
            await app.send_message(chat_id=message.chat.id, text="""Не могу добавить, так как тебя запрещено приглашать в беседы.

Что бы это исправить переходи в настройки телеграма:

- Конфидециальность
- Группы и каналы
И добавь меня в список тех, кто тебя может приглашать в группы и каналы)
Либо, открой доступ для всех, так
быстрей 😅

После этого напиши мне, и мы повторим попытку😎""")
        await app.copy_message(chat_id=message.chat.id, from_chat_id=voice_chat_id,message_id=17)


    if message.from_user.id == my_id and message.text == 'Вввв':
        await app.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)
        await app.copy_message(chat_id=message.chat.id, from_chat_id=voice_chat_id, message_id=13)

    if message.from_user.id == my_id and message.text == 'Сделать группу основной':

        id_chat = (message.chat.id)
        for id in session_ids:
            try:
                await app.get_chat_member(chat_id=id_chat,user_id=id)

            except: #Если ошибка - добавляем чела в чат
                try:
                    await app.add_chat_members(chat_id=id_chat, user_ids=id)
                    await asyncio.sleep(1)
                except:
                    pass



app.run()