from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from bot.db import connect_db, register_user, get_balance
from bot.keyboards import stake_keyboard, card_grid_keyboard, accept_card_keyboard
from bot.config import ADMIN_USER_ID

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    conn = await connect_db()
    await register_user(conn, message.from_user.id)
    await message.answer("እንኳን ደህና መጡ! Welcome to Bingo 🎉\nYou’ve been given 10 ETB to start playing.")

@router.message(Command("balance"))
async def balance_handler(message: Message):
    conn = await connect_db()
    balance = await get_balance(conn, message.from_user.id)
    await message.answer(f"Your current balance is: {balance} ETB")

@router.message(Command("play"))
async def play_handler(message: Message):
    await message.answer("Choose your stake:", reply_markup=stake_keyboard())

@router.callback_query(F.data.startswith("stake_"))
async def stake_selected(callback: CallbackQuery):
    stake = int(callback.data.split("_")[1])
    await callback.message.answer(f"Stake selected: {stake} ETB\nPick a card:", reply_markup=card_grid_keyboard())

@router.callback_query(F.data.startswith("card_"))
async def card_selected(callback: CallbackQuery):
    card = int(callback.data.split("_")[1])
    await callback.message.answer(f"You selected card {card}. Confirm?", reply_markup=accept_card_keyboard())

@router.callback_query(F.data == "accept_card")
async def accept_card(callback: CallbackQuery):
    await callback.message.answer("Card locked! Waiting for game to start...")

@router.callback_query(F.data == "cancel_card")
async def cancel_card(callback: CallbackQuery):
    await callback.message.answer("Card selection canceled. Choose again:", reply_markup=stake_keyboard())
