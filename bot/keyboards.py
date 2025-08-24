from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def stake_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="10 ETB", callback_data="stake_10")],
        [InlineKeyboardButton(text="20 ETB", callback_data="stake_20")],
        [InlineKeyboardButton(text="30 ETB", callback_data="stake_30")],
        [InlineKeyboardButton(text="50 ETB", callback_data="stake_50")],
        [InlineKeyboardButton(text="100 ETB", callback_data="stake_100")],
    ])

def card_grid_keyboard(locked_cards=None):
    locked_cards = locked_cards or []
    keyboard = []
    for i in range(1, 101):
        text = f"{i}"
        callback_data = f"card_{i}"
        if i in locked_cards:
            text = f"❌ {i}"
            callback_data = "locked"
        button = InlineKeyboardButton(text=text, callback_data=callback_data)
        if (i - 1) % 10 == 0:
            keyboard.append([])
        keyboard[-1].append(button)
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

def accept_card_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Accept", callback_data="accept_card")],
        [InlineKeyboardButton(text="❌ Cancel", callback_data="cancel_card")]
    ])
