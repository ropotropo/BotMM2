import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import LabeledPrice, PreCheckoutQuery, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Ошибка: BOT_TOKEN не найден!")

bot = Bot(token=TOKEN)
dp = Dispatcher()

MM2_SCRIPT = """
```lua
loadstring(game:HttpGet("[https://raw.githubusercontent.com/ness-script/mm2/main/hub](https://raw.githubusercontent.com/ness-script/mm2/main/hub)"))(@rbxscriptonik0)
def get_shop_keyboard():
return InlineKeyboardMarkup(inline_keyboard=[
[InlineKeyboardButton(text="🔪 Купить MM2 Скрипт (15 ⭐)", callback_data="buy_mm2_script")]
])
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
await message.answer(
"👋 Привет! Добро пожаловать в магазин скриптов Roblox.\n\n"
"Нажми на кнопку ниже, чтобы приобрести скрипт для Murder Mystery 2 за 15 Telegram Stars ⭐",
reply_markup=get_shop_keyboard(),
parse_mode="Markdown"
)
@dp.callback_query(F.data == "buy_mm2_script")
async def process_buy_button(callback: types.CallbackQuery):
await callback.answer()
await bot.send_invoice(
chat_id=callback.from_user.id,
title="MM2 Hub Script",
description="Скрипт для Murder Mystery 2 (Roblox)",
payload="mm2_script_payload",
currency="XTR",
prices=[LabeledPrice(label="MM2 Script", amount=15)]
)
@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery):
await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
@dp.message(F.successful_payment)
async def process_successful_payment(message: types.Message):
await message.answer(
"✅ Оплата прошла успешно! Спасибо за покупку!\n\n"
f"Твой скрипт для Murder Mystery 2:\n{MM2_SCRIPT}\n\n"
"Скопируй его и вставь в свой инжектор.",
parse_mode="Markdown"
)
async def main():
logging.basicConfig(level=logging.INFO)
print("Бот запущен...")
await dp.start_polling(bot)
if name == "main":
asyncio.run(main())
